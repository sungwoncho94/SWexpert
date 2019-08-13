T = int(input())

for t in range(1, T+1):
    origin = list(map(str, input()))
    test = input()

    origin_list = []

    for o in origin:
        if o not in origin_list:
            origin_list.append(o)
    
    temp = 0
    result = 0

    for i in origin_list:
        temp = test.count(i)
        
        if temp >= result:
            result = temp

    print(f'#{t} {result}')

    