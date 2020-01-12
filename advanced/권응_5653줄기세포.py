from collections import deque
near = [[-1,0], [0,1], [1,0], [0,-1]]

for t in range(int(input())):
    q = deque()
    bd = [[0]*700 for i in range(700)]
    vis = [[0]*700 for i in range(700)]
    n,m,k = map(int,input().split())
    st_po = 310
    sepo = 0
    for x in range(n):
        data = list(map(int,input().split()))
        for y in range(m):
            if data[y] > 0:
                bd[st_po+x][st_po+y] = data[y]
                q.append([st_po+x,st_po+y,data[y]])
                sepo += 1
    for i in range(k):
        new = deque()
        for _ in range(len(q)):
            x,y,jul = q.popleft()
            hal = bd[x][y]
            if bd[x][y] > 0:
                bd[x][y] -= 1
                if bd[x][y] == 0:
                    bd[x][y] = -1
                q.append([x,y,jul])
            else:
                if bd[x][y] == -1:
                    for a,b in near:
                        xi, yi = a+x, b+y
                        if bd[xi][yi] == 0:
                            if vis[xi][yi] > 0:
                                vis[xi][yi] = max(jul,vis[xi][yi])
                            else:
                                vis[xi][yi] = jul
                            new.append([xi,yi])
                jul -= 1
                bd[x][y] -= 1
                if jul < 1:
                    sepo -= 1
                else :
                    q.append([x,y,jul])
        for x,y in new:
            if bd[x][y] == 0:
                bd[x][y] = vis[x][y]
                q.append([x,y,vis[x][y]])
                sepo += 1
            vis[x][y] = 0
    print('#{} {}'.format(t+1, sepo))