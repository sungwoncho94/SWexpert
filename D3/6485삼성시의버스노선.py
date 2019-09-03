T = int(input())

for t in range(1, T+1):
    N = int(input())  # 버스 노선 개수
    bus_station = [0] * 5000  # 버스 정류장은 5000개  (1~5000idx)
    result = []

    for n in range(N):
        A1, B1 = map(int, input().split())
        
        for i in range(A1, B1+1):
            bus_station[i-1] += 1

    P = int(input())
    for p in range(P):
        C = int(input())
        result.append(bus_station[C-1])

    print('#{} {}'.format(t, ' '.join(map(str, result))))