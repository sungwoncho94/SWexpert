import sys
# sys.stdin = open('input5653.txt', 'r')

def matprint(matrix):
    for a in range(len(matrix)):
        print(matrix[a])

def extend_up(mat):
    add_list = [0] * max_m
    mat.insert(0, add_list)

def extend_down(mat):
    add_list = [0] * max_m
    mat.append(add_list)

def extend_left(mat):
    for n in range(max_n):
        mat[n].insert(0, 0)

def extend_right(mat):
    for n in range(max_n):
        mat[n].append(0)

T = int(input())

for t in range(1, T+1):
    result = 0
    result2 = 0

    N, M, K = map(int, input().split())
    # N : 세로줄 / M : 가로줄 / K : hour

    max_n = N  # max_n : 최대 세로 줄
    max_m = M  # max_m : 최대 가로 줄

    hour = 0
    matrix = []
    state = [[0]*M for _ in range(N)]

    # 하, 우, 상, 좌 네 방향 탐색
    dir_i = [1, 0, -1, 0]
    dir_j = [0, 1, 0, -1]

    # matrix 만들기
    for n in range(N):
        temp_list = list(map(int, input().split()))
        matrix.append(temp_list)

    # matrix에 있는 세포를 state에 옮겨주기 (세포크기 + 1 = 활성화 시간)
    for i in range(N):  # 세로
        for j in range(M):  # 가로
            if matrix[i][j] > 0:
                state[i][j] = matrix[i][j] + 1
                result2 += 1

    while hour < K:
        # print('==========', 'hour', hour, '==========')
        # 확장해야하는 칸이 있는지부터 확인하자
        # print('state')
        # matprint(state)
        for a in range(max_m):
            if state[0][a] == 1:
                extend_up(matrix)
                extend_up(state)
                max_n += 1
                break

        for b in range(max_m):
            if state[max_n -1][b] == 1:
                extend_down(matrix)
                extend_down(state)
                max_n += 1
                break

        for c in range(max_n):
            if state[c][0] == 1:
                extend_left(matrix)
                extend_left(state)
                max_m += 1
                break

        for d in range(max_n):
            if state[d][max_m - 1] == 1:
                extend_right(matrix)
                extend_right(state)
                max_m += 1
                break

        for i in range(max_n):  # 세로
            for j in range(max_m):  # 가로
                # state == 1일때만 (번식을 해야 할 때만) 코드를 진행
                if state[i][j] != 1 :
                    continue
                # state == 1인 좌표의 하, 우, 상, 좌 방향으로 살펴본다
                for dir in range(4):
                    dx = dir_i[dir] + i
                    dy = dir_j[dir] + j
                    # 번식하는 세포 주변이 빈공간이라면, 번식세포의 크기만큼 퍼뜨린다.
                    # 이 때, matrix는 세포로 채워지지만 state의 주변은 채워지지 않는다
                    # -> state가 0인 부분을 기준으로 삼아서, 원래 있던 세포와 새로 번식하려는 세포의 크기를 비교하여 번식시킨다
                    if state[dx][dy] == 0:
                        matrix[dx][dy] = max(matrix[i][j], matrix[dx][dy])
                # 네방향 번식이 끝나면, 번식이 끝난 세포는 죽은 세포로 바꾼다
                matrix[i][j] = -1
                state[i][j] = -1


        for i in range(max_n):
            for j in range(max_m):
                # 번식이 끝난 후, state값을 1씩 줄여주기
                if state[i][j] > 0:
                    state[i][j] -= 1
                # 새로 확장된 부분에 대해 matrix -> state로 값 가져오기
                if state[i][j] == 0 and matrix[i][j] > 0:
                    state[i][j] = matrix[i][j] + 1
        
        hour += 1
        print("-------hour-------", hour)
        matprint(matrix)
        print('state')
        matprint(state)

    for i in range(max_n):
        for j in range(max_m):
            if state[i][j] > 0:
                result += 1

    print('#{} {}'.format(t, result))
    #print('#{} {}'.format(t, result2))


# 문제점 : 예시2번 hour = 4 의 모양이 틀리다.
# 활성화되어 번식 된 세포를 바로 죽여버린 것이 문제 -> 수정