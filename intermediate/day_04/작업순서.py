def dfs(node):
    # visited == 0인 node를 스택에 쌓는다
    stack = []
    path = ''
    stack.append(node)

    while stack:  # stack의 개수가 0이면 계속돌림
        for i in range(len(stack)):
            state = stack.pop()  # 나의 현재 위치 node
            if visited[state] > 0:  # 나에게 들어올 node가 남아있다면,
                visited[state] -= 1  # 방문하고, visited -1하기
            else:  # 더이상 나에게 들어올 노드가 없다면,
                visited[state] = 'Fin'  # visit을 Fin으로 바꾸기
                path += str(state)  # 자신에게 들어오는 노드가 없다면, path로 등록
                path += ' '
                stack.extend(adj[state])  # 주변탐색 = 나에게 들어오는 노드는 없으니까, 내가 갈 수 있는 노드 찾기
    return path



for t in range(1, 11):
    V, E = map(int, input().split())
    line = list(map(int, input().split()))
    start = []
    end = []
    adj = [[] for i in range(V+1)]

    for l in range(len(line)):
        start.append(line[l]) if l % 2 == 0 else end.append(line[l])
    # print(start, end)
    # adj 리스트
    for e in range(E):
        adj[start[e]].append(end[e])

    # visited 리스트
    visited = [0] * (V+1)
    for i in range(V+1):
        visited[i] = end.count(i)
    # print(visited)

    dfs_v = ''  # result
    for i in range(1, V+1):
        if visited[i] == 0:
            dfs_v += dfs(i)
    print('#{} {}'.format(t, dfs_v))
