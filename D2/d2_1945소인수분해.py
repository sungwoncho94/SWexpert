T = int(input())
for t in range(1, T+1):
    a = b = c = d = e = 0
    num = int(input())


# 1번


    while num > 1:
        if num % 2 == 0:
            a += 1
            num /= 2
        if num % 3 == 0:
            b += 1
            num /= 3
        if num % 5 == 0:
            c += 1
            num /= 5
        if num % 7 == 0:
            d += 1
            num /= 7
        if num % 11 == 0:
            e += 1
            num /= 11
    print(a, b, c, d, e)




'''2번
    while num % 2 == 0:
        a += 1
        num /= 2
    while num % 3 == 0:
        b += 1
        num /= 3
    while num % 5 == 0:
        c += 1
        num /= 5
    while num % 7 == 0:
        d += 1
        num /= 7
    while num % 11 == 0:
        e += 1
        num /= 11
    print(a, b, c, d, e)
'''

''' 3번
    num_list = [2, 3, 5, 7, 11]
    for t in range(1, T+1):
        r = []
        num = int(input())
        while num > 1:
            for i in range(len(num_list)):
                while num % num_list[i] == 0:
                    r.append(num_list[i])
                    num /= num_list[i]
    print(f'#{t} {r.count(2)} {r.count(3)} {r.count(5)} {r.count(7)} {r.count(11)}')`
'''