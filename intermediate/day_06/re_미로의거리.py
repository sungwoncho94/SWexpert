T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]  # 상, 우, 하, 좌

def isOK(x, y):
    if x < 0 or x > N-1 or y < 0 or y > N-1 or matrix[x][y] == 1:
        return False
    return True

for t in range(1, T+1):
    N = int(input())
    matrix = []
    distance = [[0] * (N+1) for _ in range(N+1)]
    answer = 0  # 정답이 발견되면 answer = 1 이 될 것.

    for n in range(N):
        n_list = list(map(int, input()))
        matrix.append(n_list)

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start_i = i
                start_j = j

    Q = []  # 앞으로 갈 경로를 저장해둠
    visited = []  # 이미 간 좌표를 저장

    Q.append([start_i, start_j])  # 시작점 Q에 저장

    #print(state_i, state_j)

    while Q:  # Q가 빌때까지 돌림
        if answer == 1:
            break
        # (1) Q.pop해서 내가 가야하는 곳을 정해줌
        state = Q.pop(0)
        state_i = state[0]
        state_j = state[1]

        # state를 간 곳에 저장
        visited.append([state_i, state_j])

        # 상하좌우 갈 수 있는 길 검색
        for d in range(4):
            next_i = state_i + di[d]
            next_j = state_j + dj[d]

            # 갈 수 있는 길이고, 가지 않았던 곳이면 Q에 저장
            if isOK(next_i, next_j) == True and [next_i, next_j] not in visited:
                Q.append([next_i, next_j])
                distance[next_i][next_j] = distance[state_i][state_j] + 1

                # 사방 탐색하다가 3이 나오면 정답임
                if matrix[next_i][next_j] == 3:
                    result = distance[next_i][next_j] -1
                    answer = 1
                    break
    
    # while 문이 끝났는데 answer이 발견 안되면
    if answer == 0:
        result = 0

    print('#{} {}'.format(t, result))




