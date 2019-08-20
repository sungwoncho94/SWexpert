'''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6
2
7 4
1 6
2 3
2 6
3 5
2 5
3
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''
# dfs 함수 작성 - 재귀
'''
def dfs_visit(adj, u, visit):
    visit.append(u)
    for v in adj[u]:
        if v not in visit:
            dfs_visit(adj, v, visit)

def dfs(adj, s):
    visit = []
    dfs_visit(adj, s, visit)
    return visit
'''
# dfs 함수 작성 - stack
def DFS(adj):
    visit = [0] * (V + 1)
    stack = [start]
    while stack:  # stack이 차있을때까지 계속 돌림
        node = stack.pop()
        if not visit[node]:
            visit[node] = 1
            # 출발~도착까지 모든 경로가 나왔다면 끝내기
            if visit[start] == 1 and visit[end] == 1:
                return 1
            stack.extend(adj[node])  # 가지 않았던 node를 추가하여 새로운 길 만들기
    return 0
        


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    node_list = []
    adj = [[] for i in range(V+1)]

    # 가영이의 board와 똑같음
    for e in range(E):
        s_e = list(map(int, input().split()))
        node_list.append(s_e)
    # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    start, end = map(int, input().split())

    # adj 만들기
    for n in node_list:
        adj[n[0]].append(n[1])
    # [[], [4, 3], [3, 5], [], [6], [], []]

    print('#{} {}'.format(t, DFS(adj)))


    
    

