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
    if state[i][j] == 1 and matrix[i][j] == max_num:
        1. 큰 숫자부터 번식되게 만든다, 최대 생명력은 10
        2. 확장이 완료된 matrix는 'X'로 바꾼다 (죽은 세포)

4. 새롭게 번식된 줄기세포를 state에 채워준다
    if state[i][j] == 0 and matrix[i][j] > 0:
        staet[i][j] = matrix[i][j] + 1
5. while hour <= K: 일 때 까지 돌리기
'''
def matprint(matrix):
    for a in range(N):
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
    N, M, K = map(int, input().split())
    # N : 세로줄 / M : 가로줄 / K : hour

    max_n = N  # max_n : 최대 세로 줄
    max_m = M  # max_m : 최대 가로 줄

    hour = 0
    matrix = []
    state = [[0]*M for _ in range(N)]
    for n in range(N):
        temp_list = list(map(int, input().split()))
        matrix.append(temp_list)

    for i in range(N):  # 세로
        for j in range(M):  # 가로
            if matrix[i][j] > 0:
                state[i][j] = matrix[i][j] + 1
    matprint(matrix)
    extend_up(matrix)
    extend_left(matrix)
    matprint(matrix)
    # while hour <= K:
    #     # 확장해야하는 칸이 있는지부터 확인하자
    #     for i in range(N):
    #         for j in range(M):
    #             if state[i][j] == 1:
    #                 if i == 0:
    #                     extend_up()


