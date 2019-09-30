'''
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1


#1 7
#2 11
'''

T = int(input())

for t in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))

    result_list = []

    for b in range(2**N):
        temp_sum = 0
        bin_list = [0] * N
        str_bin = str(bin(b))[2:]
       # print('str_bin=',str_bin)

        for b in range(len(str_bin)):
            bin_list[N-len(str_bin)+b] = int(str_bin[b])

        for a in range(len(bin_list)):
            temp_sum += bin_list[a] * n_list[a]

        if temp_sum not in result_list:
            result_list.append(temp_sum)

    print('#{} {}'.format(t, len(result_list)))