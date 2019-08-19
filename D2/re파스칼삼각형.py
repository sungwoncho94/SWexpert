T = int(input())

for t in range(1, T+1):
    N = int(input())
    total_list = []

    print('#{}'.format(t))
    for i in range(N):  # N = 4 --> 0, 1, 2, 3
        n_list = []
        for j in range(i+1):  # j = 0 / 0, 1 / 0, 1, 2 / 0, 1, 2, 3 -> N과 개수가 같아짐
            if j == 0:
                n_list.append(1)
            elif j == i:
                n_list.append(1)
            else:
                n_list.append(total_list[i-1][j] + total_list[i-1][j-1])

        for n in n_list:
            print(n, end=" ")
        print()
        total_list.append(n_list)
