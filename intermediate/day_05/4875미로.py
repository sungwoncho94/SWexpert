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
                i = a
                j = b
                break
    
    state = matrix[i][j]
    stack = []
    


>>>>>>> b35f0f215c5758d6a3da4a253a3ce18a0cefa37d
