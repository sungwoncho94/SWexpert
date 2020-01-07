'''
0.1 extend_up / down / left / right 함수 만들기
0.2 matrix / state 두 개의 매트릭스를 만든다
0.3 max_n = N / max_m = M  (idx 기준 아님)

1. matrix -> state 복사한다. 이 때, 0보다 큰 값에 대하여 n+1을 한다
2. state를 돌면서 모든 값을 -1을 한다
3. 이 때, 1 -> 0이 되는 칸이 있는지 확인
3.1 state / matrix 함께 확장한다
    n = 0인 칸이 1일 때 -> 위에 [0] * M list 추가
    n = max_n - 1 칸이 1일 때 -> 아래에 [0] * M list 추가
    m = 0인 칸이 1일 때 -> 각 matrix 리스트를 돌면서 왼쪽에 한 칸 추가
    m = max_m -1 칸이 1일 때 -> 오른쪽에 한 칸씩 추가
    (모두 extend_ 함수를 사용해서 하기)
3.2 다시 state를 살펴보면서, 1-> 0 인 칸이 있으면...
    if state[i][j] == 1 and matrix[i][j] == num:
        1. 큰 숫자부터 번식되게 만든다, 최대 생명력은 10
        2. 확장이 완료된 matrix는 'X'로 바꾼다 (죽은 세포)

4. 새롭게 번식된 줄기세포를 state에 채워준다
    if state[i][j] == 0 and matrix[i][j] > 0:
        staet[i][j] = matrix[i][j] + 1
5. while hour <= K: 일 때 까지 돌리기
'''
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

T = int(input())

for t in range(1, T+1):
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

    while hour <= K:
        # 확장해야하는 칸이 있는지부터 확인하자
        for j in range(M):
            if state[0][j] == 1:
                extend_up(matrix)
                extend_up(state)
                max_n += 1
                break

        for j in range(M):
            if state[max_n -1][j] == 1:
                extend_down(matrix)
                extend_down(state)
                max_n += 1
                break

        for i in range(N):
            if state[i][0] == 1:
                extend_left(matrix)
                extend_left(state)
                max_m += 1
                break
        
        for i in range(N):
            if state[i][max_m - 1] == 1:
                extend_right(matrix)
                extend_right(state)
                max_m += 1
                break
        
        # state에서 1인 값을 찾아서 번식
        # 이 때, matrix값이 큰 것부터 찾아서 번식시켜야 한다
        # matrix에서 번식이 완료된 칸은 'X'로 표시하기
        # state == 1이었던 칸은 0으로 만든다
        # 모든 번식이 끝난 후, state에서 0보다 큰 값들을 -1 한다
        # matrix -> state로 다시 옮겨오기
        for i in range(max_n):
            for j in range(max_m):
                if state[i][j] == 1:
                    for num in range(10, 0, -1):
                        if matrix[i][j] == num:
                            for dir in range(4):
                                xi = dir_i[dir] + i
                                yi = dir_j[dir] + j

                                if in_matrix(xi, yi) and matrix[xi][yi] == 0:
                                    matrix[xi][yi] = matrix[i][j]

                                xi -= dir_i[dir]
                                yi -= dir_j[dir]
                            matrix[i][j] = 'X'
                    state[i][j] = 'X'

        for i in range(max_n):
            for j in range(max_m):
                # 새로 확장된 부분에 대해 matrix -> state로 값 가져오기
                if state[i][j] == 0 and matrix[i][j] > 0:
                    state[i][j] = matrix[i][j] + 1
                # 
                if state[i][j] > 0:
                    state[i][j] -= 1

        hour += 1

        print('==============================')
        matprint(matrix)
                                



                            





