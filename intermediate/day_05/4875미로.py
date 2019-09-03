<<<<<<< HEAD
for t in range(int(input())):
    board = []
    N = int(input())
    for n in range(N):
        board.append(list(map(int, input())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                stack.append([i, j]) 
    result = 0
    while stack:
        x, y = stack.pop()
        for idx in range(4):
            xi = x + dx[idx]
            yi = y + dy[idx]
            if 0 <= xi < N and 0 <= yi < N:
                if board[xi][yi] == 0:
                    stack.append([xi, yi])
                    board[xi][yi] = 1
                elif board[xi][yi] == 3:
                    result = 1
                    stack = []
                    break
                            
    print(result)
=======
'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''


# 해당 좌표가 이동 가능한지 여부 판별
# 테두리 벗어나지 않고, 가보지 않은 곳 가고, 1(벽)도 가면 X
def is_ok(y, x):
    return 0 <= y < n and 0 <= x < n and matrix[y][x] != 1:
        # return True


# Y좌표, X좌표 순서임
# 재귀함수 작성
def find_map(startY, startX):
    global result
    # 1. 종료조건 설정
    if matrix[startY][startX] == 3:
        result = 1
        return result  # 전역변수로 바꿔줘야함 --> global 사용
    
    # 2. 반복검색 (4방향 검색)

    # visited 설정 (간곳이 3이 아니면, visited에 추가)
    visited.append((startY, startX))

    # 답을 찾았으면 멈춰줘야함 --> 답을 찾지 않았고 & 갈 수 있는 길이면 시행
    if result == 0 and is_ok(startY, startX + 1) and (startY, startY + 1) not in visited:
        find_map(startY, startX + 1)  # 우측
    if result == 0 and is_ok(startY + 1, startX) and (startY + 1, startY) not in visited:
        find_map(startY + 1, startX)  # 아래
    if result == 0 and is_ok(startY, startX - 1) and (startY, startY - 1) not in visited:
        find_map(startY, startX - 1)  # 좌측
    if result == 0 and is_ok(startY - 1, startX) and (startY - 1, startY) not in visited:
        find_map(startY - 1, startX)  # 위




T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = []

    # matrix 완성
    # matrix = [[1, 3, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 2, 1]]
    for n in range(N):
        m_list = list(map(int, input()))
        matrix.append(m_list)
    

    # 시작 idx 구하기
    for a in range(N):
        for b in range(N):
            if matrix[a][b] == 2:
                startX = a
                startY = b
                break
    # 방문했던 위치 저장소 필요 --> visited
    visited = []
    # 목적지 도착 여부
    result = 0
    
    
    


>>>>>>> b35f0f215c5758d6a3da4a253a3ce18a0cefa37d
