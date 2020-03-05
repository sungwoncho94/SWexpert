def cost(u, fee):
    global total

    if fee > total:
        return

    elif u > 12:
        if total > fee:
            total = fee

    else:
        if u + 1 != 0:
            cost(u + 1, fee + day * use[u])
            cost(u + 1, fee + month)
            cost(u + 3, fee + threemonth)

for t in range(int(input())):
    day, month, threemonth, year = map(int, input().split())
    use = [0] + list(map(int, input().split()))

    total = year
    cost(0, 0)

    print('#{} {}'.format(t+1, total))