'''
10
4
0100
1110
1011
1010
6
011001
010100
010011
101001
010101
111010

# 1 2
# 2 2
'''

T = int(input())


for t in range(1, T+1):
    N = int(input())
    matrix = []
    Q = []
    visit = [[0] * N for _ in range(N)]


    for n in range(N):
        temp = list(str(input()))
        matrix.append([])
        for t in temp:
            matrix[n].append(int(t))
    # print(matrix)

    for i in range(N):
        for j in range(N):
            



        
        

