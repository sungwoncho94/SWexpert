T = int(input())
for t in range(1, T+1):
    result = ''
    case = int(input())
    for c in range(case):
        alp, num = map(str, input().split())
        result += alp * int(num)

    print('#{}'.format(t))
    cnt = 0
    for r in result:
        if cnt < 10:
            print(r, end="")
            cnt += 1
            if cnt == 10:
                print()
                cnt = 0
    print()