T = int(input())
for t in range(1, T+1):
    D = int(input()); price = list(map(int, input().split()))
    profit = max_num = 0

    for p in range(len(price)-1, -1, -1):
        if max_num <= price[p]:
            max_num = price[p]
        else:
            profit += max_num - price[p]

    print(f'#{t} {profit}')

'''
for t in range(int(input())):
    input();a=[*map(int,input().split())];r=m=0
    for i in a[::-1]:
        if i>m:m=i
        r+=m-i
    print(f'#{t+1} {r}')
 '''