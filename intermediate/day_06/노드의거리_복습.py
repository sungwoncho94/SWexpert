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

''' 틀린버전
# BFS를 사용하여 노드의 거리를 구할 때는 depth를 올려가는 것 보다,
# distance[ ]를 만들어서 이동할 때 마다 시작노드에서부터의 거리를 구하는 것이 낫다.

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split()) # V = 노드 수, E = 간선 수
    adj = [[] for _ in range(V+1)]  # 현재 idx에서 갈 수 있는 V표시
    visited = [0] * (V+1)
    distance = [0] * (V+1)
    Q = []

    for e in range(E):
        temp = list(map(int, input().split()))
        adj[temp[0]].append(temp[1])
        adj[temp[1]].append(temp[0])

#    print(adj) = [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    start, end = map(int, input().split())
    # Q에 시작V 넣어놓고 시작
    Q.append(start)

    while Q:
       # print('Q', Q)
        node = Q.pop(0)
        # 현재 노드가 가지 않을곳일때에만, (간 곳을 또 가면 최적이 아님)
        if visited[node] == 0:
            visited[node] = 1
            # 현재 노드에서 갈 수 있는 곳에 현재까지 거리 +1만큼 해주기
            for a in adj[node]:
                distance[a] = distance[node] + 1
                Q.append(a)

        ## 틀린 이유 : 1 -> 4 -> 1로 돌아오는 과정에서
        ## 현재 node = 4이지만 distance[1]을 처리하도록 했음. node = 1이지만 distance[1] += 1이 된 것
        ## 현재 node에 대해서만 visited와 distance처리를 해줘야한다.

        print('node', node)
        print('visited', visited)
        print('distance', distance)

        # 만약 출발, 도착 노드를 모두 방문했다면 바로 끝내기
        if visited[start] == 1 and visited[end] == 1:
            break
        

    print('#{} {}'.format(t, distance[end]))
    '''

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

# BFS를 사용하여 노드의 거리를 구할 때는 depth를 올려가는 것 보다,
# distance[ ]를 만들어서 이동할 때 마다 시작노드에서부터의 거리를 구하는 것이 낫다.

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split()) # V = 노드 수, E = 간선 수
    adj = [[] for _ in range(V+1)]  # 현재 idx에서 갈 수 있는 V표시
    visited = [0] * (V+1)
    distance = [0] * (V+1)
    Q = []

    for e in range(E):
        temp = list(map(int, input().split()))
        adj[temp[0]].append(temp[1])
        adj[temp[1]].append(temp[0])

#    print(adj) = [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    start, end = map(int, input().split())
    # Q에 시작V 넣어놓고 시작
    Q.append(start)
    visited[start] = 1

    while Q:
       # print('Q', Q)
        node = Q.pop(0)
    
        # 현재 노드에서 갈 수 있는 곳에 현재까지 거리 +1만큼 해주기
        for a in adj[node]:
            # 현재 노드가 가지 않을곳일때에만, (간 곳을 또 가면 최적이 아님)
            if visited[a] == 0:
                visited[a] = 1
                distance[a] = distance[node] + 1
                Q.append(a)

        print('node', node)
        print('visited', visited)
        print('distance', distance)

        # 만약 출발, 도착 노드를 모두 방문했다면 바로 끝내기
        if visited[start] == 1 and visited[end] == 1:
            break
        

    print('#{} {}'.format(t, distance[end]))
