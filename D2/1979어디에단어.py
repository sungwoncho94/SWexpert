
T = int(input())

# matrix만들기
for t in range(1, T+1):
    matrix = []
    N, k = map(int, input().split())
    count = 0
    result = 0
    
    for i in range(N):
        row_i = list(map(int, input().split()))
        matrix.append(row_i)

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                count += 1
            else:
                if count == k:
                    result += 1
                count = 0
        if count == k:
            result += 1
        count = 0

    for j in range(N):
        for i in range(N):
            if matrix[i][j] == 1:
                count += 1
            else:
                if count == k:
                    result += 1
                count = 0
        if count == k:
            result += 1
        count = 0

    print(f'#{t} {result}')