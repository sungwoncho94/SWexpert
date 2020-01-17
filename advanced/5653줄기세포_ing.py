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

    # matrix에 있는 세포를 state에 옮겨주기 (세포크기 = 활성화 시간)
    for i in range(N):  # 세로
        for j in range(M):  # 가로
            if matrix[i][j] > 0:
                state[i][j] = (matrix[i][j] * 2)

    while hour < K:
        print('==========', 'hour=', hour, '==========')
        # 확장해야하는 칸이 있는지부터 확인하자
        print('matrix')
        matprint(matrix)
        print('state')
        matprint(state)
        for a in range(max_m):
            if matrix[0][a] != 0 and state[0][a] == matrix[0][a]:
                extend_up(matrix)
                extend_up(state)
                max_n += 1
                break

        for b in range(max_m):
            if matrix[max_n - 1][b] != 0 and state[max_n -1][b] == matrix[max_n - 1][b]:
                extend_down(matrix)
                extend_down(state)
                max_n += 1
                break

        for c in range(max_n):
            if matrix[c][0] != 0 and state[c][0] == matrix[c][0]:
                extend_left(matrix)
                extend_left(state)
                max_m += 1
                break

        for d in range(max_n):
            if matrix[d][max_m - 1] != 0 and state[d][max_m - 1] == matrix[d][max_m - 1]:
                extend_right(matrix)
                extend_right(state)
                max_m += 1
                break
        
        for i in range(max_n):  # 세로
            for j in range(max_m):  # 가로
                # state == matrix일때만 (번식을 해야 할 때만) 코드를 진행
                # print('1111state=', state[i][j])
                if matrix[i][j] != 0 and state[i][j] == matrix[i][j]:
                # state == 1인 좌표의 하, 우, 상, 좌 방향으로 살펴본다
                    for dir in range(4):
                        dx = dir_i[dir] + i
                        dy = dir_j[dir] + j
                        # 번식하는 세포 주변이 빈공간이라면, 번식세포의 크기만큼 퍼뜨린다.
                        # 이 때, matrix는 세포로 채워지지만 state의 주변은 채워지지 않는다
                        # -> state가 0인 부분을 기준으로 삼아서, 원래 있던 세포와 새로 번식하려는 세포의 크기를 비교하여 번식시킨다
                        if state[dx][dy] == 0:
                            matrix[dx][dy] = max(matrix[i][j], matrix[dx][dy])
                
        for i in range(max_n):
            for j in range(max_m):
                # 새로 확장된 부분에 대해 matrix -> state로 값 가져오기
                if state[i][j] == 0 and matrix[i][j] > 0:
                    state[i][j] = matrix[i][j] * 2

        print('matrix')
        matprint(matrix)
        print('state')
        matprint(state)

        # 모든 state를 -= 1 해준다
        # print('state=', state[i][j])
        for i in range(max_n):
            for j in range(max_m):
                if state[i][j] > 0:
                    state[i][j] -= 1
                    if state[i][j] == 0:
                        state[i][j] = -1
                        matrix[i][j] = -1
        
        hour += 1
        # print("-------hour-------", hour)
        print('matrix')
        matprint(matrix)
        print('state')
        matprint(state)

    for i in range(max_n):
        for j in range(max_m):
            if state[i][j] > 0:
                result += 1

    print('#{} {}'.format(t, result))


# 문제점 : 예시2번 hour = 4 의 모양이 틀리다.
# 활성화된 후, n시간동안 살아있을 수 있다는 점을 간과함!!
# state의 시간을 matrix*2로 준 후, matrix값가 같아졌을 때 번식하도록 한다
# ex) matrix = 2 / state = 5 -> 1시간 후 활성화 / 2시간 대기 / state == 2가 되었을 때 번식 / 2시간 지난 후, state가 0이 될 떄 까지 살아있는 상태이다가, -1이 되면 죽음


'''
5
2 2 10
1 1
0 2
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
9 10 37                
0 0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 5 3
0 0 2 0 0 0 0 4 0 0
3 0 0 0 0 0 4 0 0 0
0 0 0 0 0 3 5 0 0 2
0 0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 2 3
0 0 0 0 0 0 0 0 0 0
0 0 2 2 0 0 0 0 0 0

#1 22
#2 36
#3 90
#4 16
#5 712
'''