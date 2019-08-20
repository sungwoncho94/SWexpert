T = int(input())

for t in range(1, T+1):
    N = int(input())
    total_list = []

    print('#{}'.format(t))

    for i in range(N):  # N = 4 -> 0 1 2 3
        n_list = []
        j = 0
        while j < i+1:  # i+1 = 1, 2, 3, 4
            if j == 0:
                n_list.append(1)
            elif j == i:
                n_list.append(1)
            else:
                n_list.append(total_list[i-1][j-1] + total_list[i-1][j])
            j += 1
        total_list.append(n_list)
        for n in n_list:
            print(n, end=" ")
        print()


