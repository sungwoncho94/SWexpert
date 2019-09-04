T = int(input())

for t in range(1, T+1):
    str_list = []
    max_str = 0
    result = []

    for _ in range(5):
        string = list(map(str, input()))
        str_list.append(string)
        if len(string) > max_str:
            max_str = len(string)

    for i in range(5):
        if len(str_list[i]) < max_str:
            while len(str_list[i]) < max_str:
                str_list[i].append('+')

    for i in range(max_str):
        for j in range(5):
            if str_list[j][i] != '+':
                result.append(str_list[j][i])
    
    print('#{} '.format(t), end="")
    for r in result:
        print(r, end='')
    print()