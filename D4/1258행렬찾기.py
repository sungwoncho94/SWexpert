T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    flag = 1
    range_list = []
    idx_list = []
    cnt = 0
    fin = False

    matrix = []
    row = 0
    # matrix작성 // row, col구하기
    for n in range(N):
        n_list = list(map(int, input().split()))
        matrix.append(n_list)
        row += 1
    col = len(n_list)

    # fin == False이면 계속 돌리고, fin == True가 되면 멈추기
    # while fin == False:
    
    cnt += 1  # 시약통 개수
    start_i = start_j = end_i = end_j = 0  # 변수 초기화
    sum_matrix = 0

    print(cnt)
    # 행 = row  /  열 = col = len(n_list)
    # start_i, start_j 구하기
    for i in range(row):
        if flag == 0:
            break
        for j in range(col):
            if matrix[i][j] != 0:
                start_i = i
                start_j = j
                flag = 0
                break
    print(start_i, start_j)
    # end_i, end_j 구하기
    end_i = start_i
    end_j = start_j
    while matrix[end_i+1][end_j] != 0:
        end_i += 1
        if end_i > row -1:
            end_i = row -1
            break

    while matrix[end_i][end_j+1] != 0:
        end_j += 1
        if end_j > col -1:
            end_j = col -1
            break
    print(start_i, start_j, end_i, end_j)
    
    # 넓이와 행렬크기 구하기
    range_list.append((end_i-start_i+1) * (end_j-start_j+1))
    idx_list.append([end_i-start_i+1, end_j-start_j+1])

    # 카운트한 시약통은 없애기
    for i in range(start_i, end_i+1):
        for j in range(start_j, end_j+1):
            matrix[i][j] = 0

    # 전체 행렬의 합이 0이 될때까지 반복
    for i in range(row):
        for j in range(col):
            sum_matrix += matrix[i][j]

    if sum_matrix == 0:
        fin = True
    else:
        fin = False

    print(matrix)
    print(range_list, idx_list)

    print('#{} {}'.format(t, cnt))
