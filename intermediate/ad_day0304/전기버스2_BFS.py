## BFS로 고치기!!

def BFS(location):
    global cnt
    state = 0

    Q = []
    Q.append(start_location)  # Q = [0]
    Q.append('cnt')
    print(Q, state, cnt)
    while Q:
        state = Q.pop(0)  # state = 0
        print('Q=', Q, 'state=', state, 'cnt=',cnt)
        
        if state == 'cnt':
            Q.append('cnt')
            cnt += 1
            state = Q.pop(0)  
            # 'cnt'를 만나면 한 층 검색을 완료한 것.
            # cnt를 하나 올려주고 다음 location을 pop해준다
        elif state == 5:
            return cnt
        else:
            for jump in graph[state]: 
                Q.append(jump)


T = int(input())

for t in range(1, T+1):
    N_list = list(map(int, input().split()))

    N = N_list[0]
    station_list = N_list[1:]  # [2, 3, 1, 1]

    # 갈 수 있는 node를 표시한 graph
    # print(graph)  = [[1, 2], [2, 3, 4], [3], [4], []]
    graph = [[] for i in range(N)]
    for i in range(N-1):
        for a in range(station_list[i]):
            graph[i].append(i+a+1)

    # 최소 충전횟수
    min_charge = 999
    # 임시 cnt는 여기서 선언해야함
    cnt = 0

    start_location = 0  # 시작노드 = 1 / location = 0

    BFS(start_location)

    print('#{} {}'.format(t, cnt))





