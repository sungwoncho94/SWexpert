T = int(input())

for t in range(1, T+1):
    N = int(input())
    max_danjo = 0
    danjo_list = []
    n_list = list(map(int, input().split()))
    result = True

    if len(n_list) == 1:
        max_danjo = -1
    else:
        for i in range(len(n_list)-1):
            for j in range((i+1), len(n_list)):
                print(i, j)
                isdanjo = str(n_list[i] * n_list[j])
                for d in range(len(isdanjo) - 1):
                    if int(isdanjo[d]) > int(isdanjo[d+1]):
                        result = False
                        break

                if result == True:
                    print(isdanjo)
                    if int(isdanjo) > max_danjo:
                        max_danjo = int(isdanjo)
    print('#{} {}'.format(t, max_danjo))