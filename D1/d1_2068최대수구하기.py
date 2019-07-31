T = int(input())

for t in range(1, T+1):
    num_list = list(map(int, input().split()))
    win = max(num_list)
    print(f'#{t} {win}')