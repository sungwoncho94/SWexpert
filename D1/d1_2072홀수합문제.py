sum_num = 0

T = int(input())                # T = 3
for t in range(1, T + 1):       # t = 1, 2, 3도는데 t = 1
    test_num = list(map(int, input().split()))    # test_num을 하나씩 입력하여 리스트를 만든다
    for i in test_num:          # test_num에 있는 수를 i 라는 변수에 차례대로 대입
        if i % 2 == 1:          # i가 홀수일때만 sum_num에 더한다
            sum_num += i        
    print(f'#{t} {sum_num}')
    sum_num = 0    
t += 1

    