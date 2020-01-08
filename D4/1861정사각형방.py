T = int(input())

for t in range(1, T + 1):
    N = int(input())
    matrix = []
    for n in range(N):
        n_list = list(map(int, input().split()))
        matrix.append(n_list)

    result_num_list = []  # list에 다 담아놓고 가장 작은 num을 꺼내자
    max_cnt = 1  # 이동할 수 있는 최대 횟수 저장

    # 0,0 ~ N-1, N-1까지 순서대로 시작해서,
    for i in range(N):
        for j in range(N):
            # 시작하는 위치 = [i, j]
            start_location = [i, j]
            a = i
            b = j  # i, j는 처음 위치만 저장해둔다. a, b로 이동할 것.
            stop = 1  # 오른쪽 왼쪽 위쪽 아래쪽이 모두 불가능하면 stop은 여전히 0이다.
            cnt = 0

            # print('시작 번호', matrix[i][j])
            # print('a, b', a, b)

            while stop == 1:
                # stop을 0으로 바꾸고 밑에서 돌려서 1이 되나 안되나 봐야한다.
                stop = 0
                # idx a+1이 N-1을 넘지 않고, 아래쪽이 현재 위치보다 1이 크다면 오른쪽으로 이동
                if (a + 1) < N:
                    # print('아래')
                    if matrix[a + 1][b] == matrix[a][b] + 1:
                        cnt += 1
                        a += 1
                        stop = 1
                    # print('아래ㅇㅋ')
                # 오른쪽
                if (b + 1) < N:
                    # print('오른쪽')
                    if matrix[a][b + 1] == matrix[a][b] + 1:
                        cnt += 1
                        b += 1
                        stop = 1
                    # print('오른쪽ㅇㅋ')
                # 위
                if (a - 1) >= 0:
                    # print('위')
                    if matrix[a - 1][b] == matrix[a][b] + 1:
                        cnt += 1
                        a -= 1
                        stop += 1
                    # print('위ㅇㅋ')
                # 왼쪽
                if (b - 1) >= 0:
                    # print('왼쪽')
                    if matrix[a][b - 1] == matrix[a][b] + 1:
                        cnt += 1
                        b -= 1
                        stop = 1
                    # print('왼쪽ㅇㅋ')

            if cnt == max_cnt:
                max_cnt = cnt
                result_num_list.append(matrix[i][j])
            elif cnt > max_cnt:
                max_cnt = cnt
                result_num_list = []
                result_num_list.append(matrix[i][j])


             #   print(cnt, result_num_list)

    result = min(result_num_list)
    print('#{} {} {}'.format(t, result, max_cnt + 1))