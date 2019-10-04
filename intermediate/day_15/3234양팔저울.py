# 왼쪽 >= 오른쪽

def fact(n):
    return n * fact(n-1) if n > 1 else 1

T = int(input())

for t in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))

    result = 0

    for i in range(2**N):
        sum_left = 0
        sum_right = 0

        num_left = 0
        num_right = 0

        left_list = []
        right_list = []

        bin_list = [0]  * N
        str_i = str(bin(i))[2:]

        for s in range(len(str_i)):
            bin_list[-1-s] = int(str_i[-1-s])

        for b in range(N):
            if bin_list[b] == 0:
                sum_left += weight[b]
                num_left += 1
                left_list.append(weight[b])
            else:
                sum_right += weight[b]
                num_right += 1
                right_list.append(weight[b])

        if sum_left >= sum_right:
            print('left', left_list, 'right', right_list)
            result += fact(num_left) + fact(num_right)
            print(result)
    print(result)



        

