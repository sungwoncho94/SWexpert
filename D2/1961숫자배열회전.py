import copy

T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = []
    re_list = []  # 90도 회전하면 나오는 숫자를 순서대로 넣은 리스트
    re_matrix = [[0] * N for n in range(N)]  # re_list를 N * N 매트리스로 만들기
    result_matrix = [[0] * N for n in range(N)]  # 
    
    #input 매트리스 생성
    for n in range(N):
        numlist = list(map(int, input().split()))
        matrix.append(numlist)
    
    row = 0
    
    # result_matrix 완성
    while row < N:
        # 첫 열의 역순으로 훑어가는 숫자리스트를 만들어서, re_matrix에 넣자.
        for i in range(0, N):  # 열은 순서대로 훑고,
            for j in range(N-1, -1, -1):  # 행은 역순으로 훑자.
                re_list.append(matrix[j][i])
        
        # 90도 회전된 re_matrix완성
        for i in range(N):
            for j in range(N):
                re_matrix[i][j] = re_list[0]
                re_list.remove(re_list[0])

        for i in range(N):
            result_matrix[i][row] = re_matrix[i]
        
        # matrix = re_matrix
        # re_matrix와 re_list 초기화
        matrix = copy.deepcopy(re_matrix)
        re_matrix = [[0] * N for n in range(N)]
        re_list = []
        row += 1
    
    print('#%d' % t)
    for i in range(N):
        for j in range(3):
            for n in range(N):
                if n == N-1:
                    print(result_matrix[i][j][n], end=' ')
                else:
                    print(result_matrix[i][j][n], end='')
        print()