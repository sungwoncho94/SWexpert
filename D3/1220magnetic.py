for t in range(1, 11):
    N = int(input())
    matrix = []
    result = 0  # result는 한 문제에 하나씩 나오는 값

    # matrix 만들기
    for n in range(N):
        n_list = list(map(int, input().split()))
        matrix.append(n_list)

    # i = 열 (세로)  /  j = 행 (가로)
    for i in range(N):
        mag_list = []
        for j in range(N):
            if matrix[j][i] == 1 or matrix[j][i] == 2:
                mag_list.append(matrix[j][i])
   
        for m in range(len(mag_list)-1):
            if mag_list[m] == 1 and mag_list[m+1] == 2:
                result += 1
    print('#{} {}'.format(t, result))



