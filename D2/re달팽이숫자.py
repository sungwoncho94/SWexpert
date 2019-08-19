T = int(input())

for t in range(1, T+1):
    N = int(input())
    x = y = i = 0

    def iswall(x, y):
        if x < 0 or x >= N:
            return True
        if y < 0 or y >= N:
            return True
        if matrix[x][y] > 0:
            return True
        return False
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 빈 N*N 리스트
    matrix = [[0 for i in range(N)] for j in range(N)]
    num_list = []
    for num in range(1, N*N + 1):
        num_list.append(num)

    for n in num_list:
        matrix[x][y] += n
        n += 1
        x += dx[i]
        y += dy[i]
        if n > N**2 + 1:
            break
        if iswall(x, y):
            x -= dx[i]
            y -= dy[i]
            i = (i+1) % 4
            x += dx[i]
            y += dy[i]

    print(f'#{t}')
    for n in range(N):
        result = matrix[n]
        if n != 0:
            print()
        for r in result:
            print(r, end=' ')
    print()
                