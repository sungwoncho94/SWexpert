def DFS(x, y, cnt):
    global result

    if cnt > result:
        return

    if 0 not in visited:
        cnt += abs(x - Home_x) + abs(y - Home_y)
        if result > cnt:
            result = cnt
        return

    for i in range(N):
        x1 = Clients[i][0]
        y1 = Clients[i][1]
        if not visited[i]:
            visited[i] = 1
            temp = abs(x-x1) + abs(y-y1)
            DFS(x1, y1, cnt+temp)
            visited[i] = 0


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = list(map(int, input().split()))
    Office_x, Office_y = Data[0], Data[1]
    Home_x, Home_y = Data[2], Data[3]
    # print(Data)

    Clients = []
    for i in range(2, N+2):
        x = Data[i*2]
        y = Data[i*2+1]
        Clients.append([x,y])

    visited = [0]*N
    # cnt = 0
    result = 987654321
    DFS(Office_x, Office_y, 0)
    print('#%d %d'%(tc, result))