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

def in_matrix(x, y):
    if 0 <= x < max_n and 0 <= y < max_m:
        return True
    return False

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

    for n in range(N):
        temp_list = list(map(int, input().split()))
        matrix.append(temp_list)

    for i in range(N):  # 세로
        for j in range(M):  # 가로
            if matrix[i][j] > 0:
                state[i][j] = matrix[i][j] + 1
                result2 += 1

    while hour < K:
        print('==========', 'hour', hour, '==========')
        # 확장해야하는 칸이 있는지부터 확인하자
        for j in range(max_m):
            if state[0][j] == 1:
                extend_up(matrix)
                extend_up(state)
                max_n += 1
                break

        for j in range(max_m):
            if state[max_n -1][j] == 1:
                extend_down(matrix)
                extend_down(state)
                max_n += 1
                break

        for i in range(max_n):
            if state[i][0] == 1:
                extend_left(matrix)
                extend_left(state)
                max_m += 1
                break
        
        for i in range(max_n):
            if state[i][max_m - 1] == 1:
                extend_right(matrix)
                extend_right(state)
                max_m += 1
                break
        
        # print('------바뀌기 전/줄추가 matrix, state ---------')
        # matprint(matrix)
        # print('---------')
        # matprint(state)
        # state에서 1인 값을 찾아서 번식
        # 이 때, matrix값이 큰 것부터 찾아서 번식시켜야 한다
        # matrix에서 번식이 완료된 칸은 'X'로 표시하기
        # state == 1이었던 칸은 0으로 만든다
        # 모든 번식이 끝난 후, state에서 0보다 큰 값들을 -1 한다
        # matrix -> state로 다시 옮겨오기
        for i in range(max_n):
            for j in range(max_m):
                if state[i][j] != 1 :
                    continue
                for dir in range(4):
                    dx = dir_i[dir] + i
                    dy = dir_j[dir] + j
                    if state[dx][dy] == 0 : #matrix[dx][dy] == 0:
                        matrix[dx][dy] = max(matrix[i][j], matrix[dx][dy])

                matrix[i][j] = -1
                state[i][j] = -1
                result2 -= 1


        for i in range(max_n):
            for j in range(max_m):
                # 번식이 끝난 후, state값을 1씩 줄여주기
                if state[i][j] > 0:
                    state[i][j] -= 1
                # 새로 확장된 부분에 대해 matrix -> state로 값 가져오기
                if state[i][j] == 0 and matrix[i][j] > 0:
                    state[i][j] = matrix[i][j] + 1
        
        hour += 1
        print("-------바뀐 후 matrix, state-------")
        matprint(matrix)
        print('state')
        matprint(state)

    for i in range(max_n):
        for j in range(max_m):
            if state[i][j] > 0:
                result += 1

    print('#{} {}'.format(t, result))
    #print('#{} {}'.format(t, result2))