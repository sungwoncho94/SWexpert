'''
2
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
#1
741 987 369
852 654 258
963 321 147
#2
872686 679398 558496
952899 979157 069877
317594 487722 724799
997427 894586 495713
778960 562998 998259
694855 507496 686278
'''
import copy

T = int(input())

for t in range(1, T+1):
    N = int(input())

    matrix = []
    re_matrix = []
    temp = []
    result_matrix = [[0] * 3 for n in range(N)]
    print(result_matrix)
    
    for n in range(N):
        n_list = list(map(int, input().split()))
        # list 1 2 3 -> relist 3 2 1 로 바꾼 후 rematrix에 append 하자
        matrix.insert(0, n_list)

        # nlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] / [[list1] [list2] [list3]]
        # matrix = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        # re_matrix = 3 [1, 2, 3], 2 [4, 5, 6], 1 [7, 8, 9]
    
    cnt = 0
    while cnt < N:
        re_matrix = list(zip(matrix[0], matrix[1]=, matrix[2]))
        for n in range(N):
            result_matrix[n][cnt] = re_matrix[n]
            temp.insert(0, re_matrix[n])
        re_matrix = temp
        
        cnt += 1
    
    print(result_matrix)


