# import sys
# sys.stdin = open("1285input.txt", "r")

T = int(input())

for t in range(1, T+1):
    People = int(input())
    distance = list(map(int, input().split()))
    abs_list = []
    short = 100000
    cnt = 0
    # print(distance)

    for d in range(People):
        temp = abs(distance[d])
        if temp < short:
            short = temp
            cnt = 1
        elif temp == short:
            short = temp
            cnt += 1
        else:
            short = short

    print('# {} {} {}'.format(t, short, cnt))
