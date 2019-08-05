# solving club제출
'''
1
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

T = 10

for t in range(1, T+1):
    Testcase = int(input())  # 1번 test case
    N = 100
    num_list = []
    matrix = []
    sum_list = []

    # 100*100 매트릭스 만들어짐
    for i in range(N):
        num_list = list(map(int, input().split()))
        matrix.append(num_list)

    # row sum구하기
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += matrix[i][j]
        sum_list.append(row_sum)
    
    # col sum구하기
    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += matrix[i][j]
        sum_list.append(col_sum)

    # eorkr1 sum구하기
    eorkr1_sum = 0
    for i in range(N):
        eorkr1_sum += matrix[i][i]
    sum_list.append(eorkr1_sum)
    
    # eorkr2 sum구하기
    eorkr2_sum = 0
    
    for i in range(N):
        j = N-i-1
        eorkr2_sum += matrix[i][j]
        print(i, j)
    sum_list.append(eorkr2_sum)

    result = max(sum_list)
    print(f'#{t} {result}')


