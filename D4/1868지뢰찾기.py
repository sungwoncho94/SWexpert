'''
2
3
..*
..*
**.
5
..*..
..*..
.*..*
.*...
.*...
'''
T = int(input())

def printmat(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

for t in range(1, T+1):
    N = int(input())
    matrix = []

    for n in range(N):
        input_str = str(input())
        temp_list = []
        for s in input_str:
            temp_list.append(s)
        matrix.append(temp_list)

'''
내가 하고싶은 것

(0,0)부터 탐색하면서 주변이 모두 .인 곳을 찾아서 터뜨림
그 주변이 또 .인 곳이 나오면 그곳을 또 터뜨림
.... 반복  -->  1 BFS
BFS한번이 끝나면 한 구역에서 나올 수 있는 최소 횟수(1번)이 나온 것 = cnt += 1

다시 (0,0)부터 탐색하면서 BFS시행

만약 BFS를 시행할 곳이 없다면(연쇄로 터뜨릴수있는 부분을 모두 터뜨렸다면)
나머지'.'숫자를 세서 cnt에 더한다
'''
def in_range(x, y):
    # 갈 수 있는 길이고 폭탄이 아니라면 True
    if 0 <= x < N and 0 <= y < N and matrix[x][y] !='*':
        return True
    return False

# 주변이 모두 .인지 확인하는 함수
def is_zero(x, y):
    if 1 <= x < N-1 and 1 <= y < N-1:
        if in_range(x-1, y) == True and matrix[x-1][y] != '*' and in_range(x+1, y) == True and matrix[x+1][y] != '*' and in_range(x, y-1) == True and matrix[x][y-1] != '*' and in_range(x, y+1) == True and matrix[x][y+1] != '*' and in_range(x-1, y-1) == True and matrix[x-1][y-1] != '*' and in_range(x-1, y+1) == True and matrix[x-1][y+1] != '*' and in_range(x+1, y-1) == True and matrix[x+1][y-1] != '*' and in_range(x+1, y+1) == True and matrix[x+1][y+1] != '*':
            return True
    # 우, 우하, 하
    elif x == 0 and y == 0:
        if in_range(x, y+1) == True and matrix[x][y+1] != '*' and in_range(x+1, y+1) == True and matrix[x+1][y+1] != '*' and in_range(x+1, y) == True and matrix[x+1][y] != '*':
            return True
    # 좌, 좌상, 상
    elif x == N-1 and y == N-1:
        if in_range(x, y-1) == True and matrix[x][y-1] != '*' and in_range(x-1, y-1) == True and matrix[x-1][y-1] != '*' and in_range(x-1, y) == True and matrix[x-1][y] != '*':
            return True
    # 상, 우상, 우
    elif x == N-1 and y == 0:
        if in_range(x-1, y) == True and matrix[x-1][y] != '*' and in_range(x-1, y+1) == True and matrix[x-1][y+1] != '*' and in_range(x, y+1) == True and matrix[x][y+1] != '*':
            return True
    # 좌, 좌하, 하
    elif x == 0 and y == N-1:
        if in_range(x, y-1) == True and matrix[x][y-1] != '*' and in_range(x+1, y-1) == True and matrix[x+1][y-1] != '*' and in_range(x+1, y) == True and matrix[x+1][y] != '*':
            return True    
    # 왼쪽벽 - 상, 우상, 우, 우하, 하
    elif y == 0:
        if in_range(x-1, y) == True and matrix[x-1][y] != '*' and in_range(x-1, y+1) == True and matrix[x-1][y+1] != '*' and in_range(x, y+1) == True and matrix[x][y+1] != '*' and in_range(x+1, y+1) == True and matrix[x+1][y+1] != '*' and in_range(x+1, y) == True and matrix[x+1][y] != '*':
            return True
    # 위쪽벽 - 좌, 좌하, 하, 우하, 우
    elif x == 0:
        if in_range(x, y-1) == True and matrix[x][y-1] != '*' and in_range(x+1, y-1) == True and matrix[x+1][y-1] != '*' and in_range(x+1, y) == True and matrix[x+1][y] != '*' and in_range(x+1, y+1) == True and matrix[x+1][y+1] != '*' and in_range(x, y+1) == True and matrix[x][y+1] != '*':
            return True
    # 오른쪽벽 - 상, 좌상, 좌, 좌하, 하
    elif y == N-1:
        if in_range(x-1, y) == True and matrix[x-1][y] != '*' and in_range(x-1, y-1) == True and matrix[x-1][y1] != '*' and in_range(x, y-1) == True and matrix[x][y-1] != '*' and in_range(x+1, y-1) == True and matrix[x+1][y-1] != '*' and in_range(x+1, y) == True and matrix[x+1][y] != '*':
            return True
    # 아래벽 - 상, 좌상, 우, 우상, 좌
    elif x == N-1:
        if in_range(x-1, y) == True and matrix[x-1][y] != '*' and in_range(x-1, y+1) == True and matrix[x-1][y+1] != '*' and in_range(x, y+1) == True and matrix[x][y+1] != '*' and in_range(x-1, y+1) == True and matrix[x-1][y+1] != '*' and in_range(x, y-1) == True and matrix[x][y-1] != '*':
            return True



for i in range(N):
    for j in range(N):
        # 주변이 모두 .이라면, 자신을 0으로 바꾸고 주변의 폭탄 개수를 센다
        if is_zero(i, j) == True:
            # 주변에 폭탄이 하나라도 발견될 때 까지 BFS를 계속 돌린다
            while is_zero(x, y) == False:
                Q = []
                Q.append((i, j))
                matrix[i][j] = 0

            




