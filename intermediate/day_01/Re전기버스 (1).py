T = int(input())

for t in range(1, T+1):
    #K, N, M = 
    jump, end, battery_number = map(int, input().split())
    battery_list = list(map(int, input().split()))
    location = 0  # 나의 위치
    cnt = 0  # 충전 횟수
    flag = 1

    while location < end:  # 내 위치가 종점과 같아지거나 넘으면 종료
        # print(location, cnt, flag)
        location += jump
        if location >= end:
            break
        if flag == 0:
            break
        cnt += 1
        if location not in battery_list:
            back = 0 # cnt >= jump : break
            for i in range(jump):
                location -= 1
                back += 1
                if back >= jump:
                    flag = 0
                    break
                elif location in battery_list:
                    break
    if flag == 1:
        print('#{} {}'.format(t, cnt))
    else:
        print('#{} 0'.format(t))

# cnt를 if문 밑으로 내리기
# 충전소에 가지 못했을 때, location -= 1 , back += 1 할 때 if 와 elif의 순서바꾸기