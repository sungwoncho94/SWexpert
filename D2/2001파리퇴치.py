T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for row in range(N):
        board.append(list(map(int, input().split())))

    row = col = result = r = c = 0
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            temp = 0
            for r in range(M):
                for c in range(M):
                    temp += board[row + r][col + c]
            if temp >= result:
                result = temp
    print(f'#{t} {result}')


