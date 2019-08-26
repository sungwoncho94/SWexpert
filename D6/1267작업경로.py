'''
9 9
4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9
5 4
1 2 2 3 4 1 1 5
'''

# (2) dfs 함수
def dfs(node):  # adj, node를 받아서 
    stack = []
    stack.append(node)  # node = 시작node (자신에게 들어오는 경로가 없는 node)
    path = ''

    while stack:
        for i in range(len(stack)):
            state = stack.pop()

            if visit[state] > 0:
                visit[state] -= 1
            if visit[state] == 0:
                visit[state] = 'fin'
                path += str(state)  # 더이상 자신에게 들어올 node가 없다면 path에 현재 node(state)를 추가
                path += ' '  # 출력형태 맞춰주기
                stack.extend(adj[state])
    return path

        

# (1) Input Data로 기초작업
T = 10
for t in range(1, T+1):
    V, E = map(int, input().split())
    n_list = list(map(int, input().split()))
    start = []
    end = []
    adj = [[] for i in range(V+1)]

    for i in range(E):
        start.append(n_list[i*2])
        end.append(n_list[i*2 + 1])
        # if i % 2 == 0:
        #     start.append(n_list[i])
        # else:
        #     end.append(n_list[i])
    # start = [4, 1, 2, 2, 5, 7, 1, 8, 8]
    # end = [1, 2, 3, 7, 6, 6, 5, 5, 9]

    # adj 만들기
    for i in range(len(start)):
        adj[start[i]].append(end[i])
    # [[], [2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]

    # visit = 해당 node로 몇 번 방문할 수 있는가?
    visit = [0] * (V+1)
    for i in range(V+1):  # 0 ~ 주어진 노드 V까지
        visit[i] = end.count(i)
    # [0, 1, 1, 1, 0, 2, 2, 1, 0, 1]

    dfs_v = ''
    for i in range(1, V+1):
        if visit[i] == 0:
            dfs_v += dfs(i)  # 시작node를 찾아서 dfs돌린 후 답에 추가
    
    print('#{} {}'.format(t, dfs_v))


