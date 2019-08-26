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
# 모든 경로를 탐색하는 DFS stack함수 만들기
def DFS(adj, start):
    visit = [0] * (V+1)  # 0을 포함한 노드들의 방문여부 리스트
    stack = []
    stack.append(start)

    while len(stack) > 0:  # == while stack:
        # (1) node정의  (stack[-1]이라고 쓸 수 없으니까)
        # stack[-1]을 제거하는 동시에, 현재node로 설정
        node = stack.pop()  
        if visit[node] == 0:
            visit[node] = 1  # node == index이므로 가능
            if visit[start] == 1 and visit[end] == 1:
                return 1
                break
        stack.extend(adj[node])  # 현재 node에서 갈 수 있는 경로를 stack에 추가
    return 0


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())  # 노드 수, 연결경로 수
    node_list = []
    adj = [[] for i in range(V+1)]  # node와 index를 동일하게 하기 위해

    for e in range(E):
        # 출발노드, 도착노드
        start_end = list(map(int, input().split()))
        node_list.append(start_end)
    # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]

    # 노드의 이웃 노드를 표시한 adj만들기
    for n in node_list:
        adj[n[0]].append(n[1])
    # [[], [4, 3], [3, 5], [], [6], [], []]

    start, end = map(int, input().split())

    result = DFS(adj, start)

    print('#{} {}'.format(t, result))

    
    

