T = int(input())

for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    #전체쪽수, a가 찾을 쪽, b가 찾을 쪽
    l, r, c = 1, P, 0
    flag_a = True
    flag_b = True
    count_a = 0; count_b = 0

    while flag_a == True:
        if Pa == c:
            flag_a = False
        c = int((l+r)/2)
        count_a += 1
        
        if Pa > c:
            l = c
            r = r

        elif Pa < c:
            l = l
            r = c
    
    l, r, c = 1, P, 0
    while flag_b == True:
        if Pb == c:
            flag_b = False
        c = int((l+r)/2)
        count_b += 1
        
        if Pb > c:
            l = c
            r = r
            
        elif Pb < c:
            l = l
            r = c

    print(count_a, count_b)
    if count_a > count_b:
        print(f'#{t} B')
    elif count_a < count_b:
        print(f'#{t} A')
    else:
        print(f'#{t} 0')