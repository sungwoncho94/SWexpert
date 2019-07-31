T = int(input())

for t in range(1, T + 1):
    num_list = []
    a = 1
    num = int(input())
    for n in range(1, num + 1):
        if a % 2 == 1:
            num_list.append(a)
        else:
            num_list.append(-a)
        a += 1
    print(f'#{t} {sum(num_list)}')