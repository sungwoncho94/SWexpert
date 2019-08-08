'''
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
'''

for t in range(1, int(input())+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    result_list = [f'#{t}']
    
    

    while len(n_list) > 0:
        # 홀수번일때는 max값
        max_num = 0
        if len(result_list) % 2 == 1:
            for n in n_list:
                #print(n_list)
                if n > max_num:
                    max_num = n
            result_list.append(max_num)
            #print(max_num)
            n_list.remove(max_num)

            # 짝수번일때는 min값
        else:
            min_num = 100
            for n in n_list:
                #print(n_list)
                if n < min_num:
                    min_num = n

            result_list.append(min_num)
            #print(min_num)
            n_list.remove(min_num)

    for i in range(11):
        print(result_list[i], end=' ')
    print()
