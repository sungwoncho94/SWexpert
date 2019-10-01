def optimal_path(x, y):
    # global 변수 꼭 써주기!
    global temp_sum, min_result

    # 가지치기
    if temp_sum > min_result:
        return

    # 모든 노드를 방문했다면 -> 마지막 계산을 해줘야한다.
    # 마지막 장소에 방문했다고 찍은 후, DFS를 한번 더 돌리기 때문
    if 0 not in visited:
        temp_sum += abs(x - home[0]) + abs(y - home[1])
        # 마지막 계산 후, min_result계산
        if temp_sum < min_result:
            min_result = temp_sum
        # 가장 하위노드에서 위로 올라갈 수 있도록 변수초기화 & return해서 재귀 끝내주기
        temp_sum -= abs(x - home[0]) + abs(y - home[1])
        return

    # 실제 재귀함수가 돌아가는 부분
    for i in range(N):
        # i번째 노드에 방문하지 않았으면,
        # 노드 옮기고, visited에 표시하고, temp_sum 계산
        if visited[i] == 0:
            visited[i] = 1
            x1 = client_x[i]
            y1 = client_y[i]
            temp_sum += abs(x - x1) + abs(y - y1)

            # 노드 다 옮긴 후, 다시 재귀
            optimal_path(x1, y1)

            # 재귀 돌린 후, 상위 노드로 돌아갈 수 있도록 변수초기화
            temp_sum -= abs(x - x1) + abs(y - y1)
            visited[i] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))

    company = [n_list[0], n_list[1]]
    home = [n_list[2], n_list[3]]
    client_list = n_list[4:]
    client_x = []
    client_y = []

    for n in range(N):
        client_x.append(client_list[2 * n])
        client_y.append(client_list[2*n + 1])

    # print(company, home, client_x, client_y) = [0, 0] [100, 100] [70, 30, 10, 90, 50] [40, 10, 5, 70, 20]

    temp_sum = 0
    min_result = 99999

    x = company[0]
    y = company[1]

    visited = [0] * N

    optimal_path(x, y)

    print('#{} {}'.format(t, min_result))
