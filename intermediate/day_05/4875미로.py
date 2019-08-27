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
    


