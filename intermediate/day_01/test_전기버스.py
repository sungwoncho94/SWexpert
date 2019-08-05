T = int(input())

for t in range(1, T+1):
    # K = 최대이동거리 / N = 총 정류장 수 / M = 충전기가 있는 정류장 번호
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    M_list.append(N)

    state = 0
    count = 0
    flag = True

    while flag == True:
        state += K
        if state in M_list:
            count += 1
            if state >= N:
                flag == False
                break

        else:
            for k in range(K-1, 0, -1):  # 2, 1
                if state + k in M_list:
                    count += 1
                    continue
                else:
                    flag == False
                    count = 0
                    break
        print(count)

                
