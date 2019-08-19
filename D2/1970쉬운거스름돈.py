T = int(input())
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    result_list = [0] * 8
    N = int(input())  # 거스름돈 가격
    temp = N

    for i in range(len(money_list)):
        while N >= money_list[i]:
            N = N - money_list[i]
            result_list[i] += 1

    print('#{}'.format(t))
    for i in result_list:
            print(i, end=" ")
    print()