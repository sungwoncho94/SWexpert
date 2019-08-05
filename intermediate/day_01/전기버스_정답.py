# 미리 충전소들의 거리를 모두 잰 후, k 이상이면 해당 충전소를 제외
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input()/split())
    charging_station = list(map(int, input().split()))
    stations = [0] * (N+1)
    for i in range(M):
        stations[charing_station[i]] == 1

    # cnt = 충전 횟수, curremt = 이동 후 위치, pre = 이동 전 위치
    cnt = cur = 0
    while(True):
        pre = cur
        cur += K
        if cur >= N:
            break
        if stations[cou] == 1:
            cnt += 1
        else:
            for i in range(1, K+1):
                if stations[cur -i] == 1:
                    cur -= i
                    cnt += 1
                    break
                if cur == pre:
                    cnt = 0
                    break
    pritn(f'#{t} {cnt}')