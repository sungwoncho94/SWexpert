def bfs(matrix, start, end):
    global distance

    Q = []
    Q.append(start)
    visit = [0] * (V+1)
    visit[start] = 1
    distance = [0] * (V+1)

    while Q:
        node = Q.pop(0)
        for v in range(V+1):
            if matrix[node][v] == 1 and visit[v] == 0:  # matrix에서 갈 수 있는 길이 있고, v가 아직 안간곳이면
                Q.append(v)
                visit[v] = 1
                distance[v] = distance[node] + 1  # v까지의 거리 = 현재노드까지의 거리 + 1

                if visit[start] == 1 and visit[end] == 1:
                    return distance[end]
    # while 문이 끝났는데도 답이 없다면 -1 return
    return 0


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    print(V, E)
    matrix = [[0] * (V+1) for _ in range(V+1)]  # 양방향으로 갈 수 있는지 없는지 나타낼 수 있음


    for i in range(E):
        node1, node2 = map(int, input().split())
        matrix[node1][node2] = 1
        matrix[node2][node1] = 1
    print(matrix)

    start, end = map(int, input().split())

    result = bfs(matrix, start, end)

    print('#{} {}'.format(t, result))


'''
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''
'''
7 4
1 6
2 3
2 6
3 5
1 5
'''

