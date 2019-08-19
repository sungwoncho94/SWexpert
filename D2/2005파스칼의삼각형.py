T = int(input())

for t in range(1, T+1):
    N = int(input())
    t_list = []

    for i in range(N):
        n_list = []
        for j in range(i+1):
            if j == 0:
                temp = 1
            elif j == i:
                temp = 1
            else:
                temp = t_list[i-1][j-1] + t_list[i-1][j]
            n_list.append(temp)
        t_list.append(n_list)
    print(t_list)
    # 시도해보기
    # i = 0
    # while i < N:
    #     while j <= i:
    #         
    # 
    #         j += 1
    #     i += 1
    
    
    # while j < i: continue   -->  이것도 해보기