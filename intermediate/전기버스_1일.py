'''
K = 한 번 충전으로 이동할 수 있는 최대 정류장 수
N = 정류장 개수 (출발지 = 0번 ~ N번 정류장까지)
M = 설치된 충전기 개수 - 충전기가 설치된 정류장 번호가 list로 주어짐
'''

T = int(input())

for t in range(1, T+1):
    # K = 최대이동거리 / N = 총 정류장 수 / M = 충전기가 있는 정류장 번호
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    M_list.append(N)

    state = 0
    count = 0
    flag = True
    
    while state < N:  # N에 도착하거나 N보다 커지면 멈춤
        state = state + K
        if state in M_list:
            count += 1
        else:
            while state not in M_list:
                state -= 1
                q = K  # 충전소를 만나면 다시 위쪽 while로 돌아가야함
                q -= 1
                if state in M_list:
                    count += 1

                if q == 0:
                    count = 0
                    flag = False
                    break

            if flag == False:
                break

    print(f'#{t} {count-1}')
