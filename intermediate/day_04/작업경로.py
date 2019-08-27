def dfs(node):


for t in range(1, 11):
    # V = node 수, E = 연결된 간선 수
    V, E = map(int, input().split())
    E_list = list(map(int, input().split()))
    start = []
    end = []
    adj = [[] for i in range(V+1)]

    for l in range(len(E_list)):
        start.append(E_list[l]) if l % 2 == 0 else end.append(E_list[l])
    
    # adj
    for e in range(E):
        adj[start[e]].append(end[e])
    # [[], [2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]

    # visited
    visited = [0] * (V+1)
    for e in range(V+1):
        visited[e] += end.count(e)
    # [0, 1, 1, 1, 0, 2, 2, 1, 0, 1]

    result = ''
    for n in range(1, V+1):
        if visited[n] == 0:
            result += dfs(n)


    
