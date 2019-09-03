T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T+1):
    N = int(input())
    matrix = [[0] * N for i in range(N)]
    num = 0
    i = j = 0
    d = 0

    while num < N * N:
        print('입력',i, j, num+1)
        num += 1
        matrix[i][j] += num
        print('계산', di[d], dj[d])
        i += di[d]
        j += dj[d]
        print('if들어가',i, j)
        if i >= N or i < 0 or j < 0 or j >= N:
            i -= di[d]
            j -= dj[d]
            d += 1
            if d == 4:
                d = 0
            i += di[d]
            j += dj[d]
            print('if_1', i, j, d)
            
        elif matrix[i][j] > 0:
            i -= di[d]
            j -= dj[d]
            d += 1
            if d == 4:
                d = 0
            i += di[d]
            j += dj[d]
            print('if_2', i, j, d)

    print(matrix)


