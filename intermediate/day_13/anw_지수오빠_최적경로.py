# spot = [[0, 0], [100, 100], [70, 40], [30, 10], [10, 5], [90, 70], [50, 20]]

def perm(k):
    global sum, min_num, temp_sum
    if k == R:
        sum = 0
        sum += abs(spot[0][0] - spot[t[0]][0]) + abs(spot[0][1] - spot[t[0]][1])
        for _ in range(len(t)-1):
            sum += abs(spot[t[_]][0] - spot[t[_ + 1]][0]) + abs(spot[t[_]][1] - spot[t[_ + 1]][1])
        sum += abs(spot[1][0] - spot[t[-1]][0]) + abs(spot[1][1] - spot[t[-1]][1])
        if sum < min_num:
            min_num = sum
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = i + 2
            if k == 0:
                temp_sum += abs(spot[0][0] - spot[t[0]][0]) + abs(spot[0][1] - spot[t[0]][1])
            else:
                temp_sum += abs(spot[t[k]][0] - spot[t[k - 1]][0]) + abs(spot[t[k]][1] - spot[t[k - 1]][1])
            visited[i] = 1
            if temp_sum > min_num:
                visited[i] = 0
                if k == 0:
                    temp_sum -= abs(spot[0][0] - spot[t[0]][0]) + abs(spot[0][1] - spot[t[0]][1])
                else:
                    temp_sum -= abs(spot[t[k]][0] - spot[t[k - 1]][0]) + abs(spot[t[k]][1] - spot[t[k - 1]][1])
                continue
            perm(k+1)
            visited[i] = 0
            if k == 0:
                temp_sum -= abs(spot[0][0] - spot[t[0]][0]) + abs(spot[0][1] - spot[t[0]][1])
            else:
                temp_sum -= abs(spot[t[k]][0] - spot[t[k - 1]][0]) + abs(spot[t[k]][1] - spot[t[k - 1]][1])
 
 
T = int(input())
 
for tc in range(1, T+1):
    clients = int(input())
    temp_spot = list(map(int, input().split()))
    spot = []
    for c in range(len(temp_spot)//2):
        spot.extend([[temp_spot[c*2], temp_spot[c*2 + 1]]])

    print(spot)
 
    N = clients
    R = clients
    visited = [0] * N
    t = [0] * R
    sum = 0
    min_num = 10000
    temp_sum = 0
 
    perm(0)
 
    print('#{} {}'.format(tc, min_num))