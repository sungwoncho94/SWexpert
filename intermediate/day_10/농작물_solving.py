T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = []
    result = 0
    cnt = 1
    col = N//2

    for n in range(N):
        n_list = list(map(int, input()))
        matrix.append(n_list)

    for row in range(N//2 + 1):
        for c in range(cnt):
            result += matrix[row][col + c]
            #matrix[row][col + c] += 100
        if col > 0:
            col -= 1
        if cnt < N:
            cnt += 2

    col += 1
    cnt -= 2
    for row in range(N//2 + 1, N + 1):
        for c in range(cnt):
            print(row, col+c)
            result += matrix[row][col + c]
        col += 1
        cnt -= 2

    print('#{} {}'.format(t, result))