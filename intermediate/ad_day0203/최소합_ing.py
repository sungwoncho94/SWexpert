T = int(input())

for t in range(1, T+1):
    N = int(input())
    num = (N-1)*2
    bin_list = [0] * num
    matrix = []
    for n in range(N):
        n_list = list(map(int, input().split()))
        matrix.append(n_list)

    for n in range(1, 2**num):
        bin_num = str(bin(n))
        bin_num = bin_num[2:]
        print(bin_num)

        for b in range(len(bin_num)):
            bin_list[b-1] = int(bin_num[b-1])
            
            if sum(bin_list) != 
        print(bin_list)



