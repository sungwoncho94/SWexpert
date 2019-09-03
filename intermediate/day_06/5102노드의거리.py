def bfs(adj, start):
    visit = [0] * V+1  # 방문한 곳을 +1할 것.
    queue = []
    temp_list = []
    queue.append(start)

    while queue:
        node = queue.pop(0)
        temp_list.extend(adj[node])
        queue.extend(adj[node])

        while temp_list:
            node = temp_list.pop(0)
            if visit[node] == 0:
                visit[node] += 1
                queue.append(node)
        if len(temp_list) == 0:
            cnt += 1
    

        


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())  # V = 노드 수, E = Edge/간선
    adj = [[] for i in range(V+1)]  # [[], [], [], []]

    for e in range(E):
        node1, node2 = map(int, input().split())
        adj[node1].append(node2)
        adj[node2].append(node1)
    # print(adj)  [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    start, end = map(int, input().split())


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

