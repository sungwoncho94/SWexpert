def isOK(x, y):
    return 0 <= y < N and 0<= x < N and (matrix[y][x] == 0 or m[y][x] == 3)

# 내가 방문한 이력과 거리를 동시에 바꾸면서 계속 길탐색
# Q를 사용하여 앞으로 갈 곳 탐색


T = int(input())

dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dy = [0, 1, 0, -1]

for t in range(1, T+1):
    N = int(input())
    distance = [[0] * N for _ in range(N)]

    matrix = []
    for n in range(N):
        n_list = list(map(int, input()))
        matrix.append(n_list)
        Q = []
        visited = []
        start_i = start_j = 0
    # (1) 출발점 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start_i = i
                start_j = j

        Q.append((start_i, start_j))
        visited.append((start_i, start_j))

        while Q:
            state_x, state_y = Q.pop(0)

            for i in range(4):
                next_x = state_x + dx[i]
                next_y = state_y + dy[i]

                if isOK(next_x, next_y) and (next_x, next_y) not in visited:
                    Q.append(next_x, next_y)
                    visited.append((next_x, next_y))
                    distance[next_x][next_y] = distance[state_x][state_y] + 1
                    if matrix[next_x][next_y] == 3:
                        result_distance = distance[next_x][next_y] - 1

        print(result_distance)


    print("#{} {}".format(t, result))
