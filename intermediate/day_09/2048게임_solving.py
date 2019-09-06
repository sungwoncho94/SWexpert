'''
8
5 up
4 8 2 4 0
4 4 2 0 8
8 0 2 4 4
2 2 2 2 8
0 2 2 0 0
2 down
16 2
0 2
4 left
2 2 2 4
4 2 0 0
0 0 8 2
0 8 8 2
4 right
2 0 2 4
2 0 4 2
2 2 4 8
2 2 4 4
6 up
2 4 0 0 4 8
2 8 0 4 0 0
2 0 8 0 0 0
2 4 0 4 8 8
2 2 2 2 4 4
8 0 0 8 0 0
6 right
2 4 0 0 4 8
2 8 0 4 0 0
2 0 8 0 0 0
2 4 0 4 8 8
2 2 2 2 4 4
8 0 0 8 0 0
6 down
2 4 0 0 4 8
2 8 0 4 0 0
2 0 8 0 0 0
2 4 0 4 8 8
2 2 2 2 4 4
8 0 0 8 0 0
6 left
2 4 0 0 4 8
2 8 0 4 0 0
2 0 8 0 0 0
2 4 0 4 8 8
2 2 2 2 4 4
8 0 0 8 0 0
'''
T = int(input())
for t in range(1, T + 1):
    temp_list = list(map(str, input().split()))
    N = int(temp_list[0])
    command = temp_list[1]
    matrix = []

    for n in range(N):
        n_list = list(map(int, input().split()))
        matrix.append(n_list)

    # up
    if command == 'up':
        for i in range(N):  # (0 ~ N-2 idx 까지) 마지막줄은 확인할 필요가 없다
            for j in range(N):
                stop = 0
                flag = 1
                if matrix[i][j] == 0:
                    for x in range(i+1, N):
                        stop += matrix[x][j]
                        if stop > 0:  # 땡겨올 숫자가 있으면
                            while matrix[i][j] == 0:  # 0 0 2 가 나올수도 있으니까, 현재 위치에 숫자가 채워질때까지
                                for a in range(i, N-1):  # 0이 나온 줄부터 끝-1줄까지
                                    matrix[a][j] = matrix[a+1][j]  # 한칸위로 땡겨오기
                                    matrix[a+1][j] = 0

                if matrix[i][j] > 0:
                    for a in range(i+1, N):  # 현재 밑줄부터 마지막줄까지 숫자가 나올때까지 탐색
                        if flag == 0:  # 한번 끌올 다 하고 멈추기
                            break
                        if matrix[a][j] != 0:  # matrix[i][j]에 숫자가 나오면
                            if matrix[i][j] == matrix[a][j]:   # 숫자가 똑같다면
                                matrix[i][j] *= 2  # 현재 위치는 X 2 하고
                                matrix[a][j] = 0  # 더해진 숫자는 0으로 바꾸기
                                flag = 0
                                break
                            else:
                                break

    # down
    if command == 'down':
        for i in range(N-1, -1, -1):  # 가장 밑줄부터 확인하자
            for j in range(N):  # j idx 방향을 그대로 왼쪽->오른쪽
                stop = 0
                flag = 1
                if matrix[i][j] == 0:
                    for x in range(i-1, -1, -1):
                        stop += matrix[x][j]
                        if stop > 0:
                            while matrix[i][j] == 0:  # 0 0 2 가 나올수도 있으니까, 현재 위치에 숫자가 채워질때까지
                                for a in range(i, 0, -1):  # i줄부터 첫줄까지
                                    matrix[a][j] = matrix[a - 1][j]  # 한칸 아래로 땡겨오기
                                    matrix[a - 1][j] = 0

                if matrix[i][j] > 0:
                    for a in range(i-1, -1, -1):  # 현재 윗줄부터 맨 윗줄까지 탐색
                        if flag == 0:  # 한번 끌올 다 하고 멈추기
                            break
                        if matrix[a][j] != 0:  # matrix[i][j]에 숫자가 나오면
                            if matrix[i][j] == matrix[a][j]:  # 숫자가 똑같다면
                                matrix[i][j] *= 2  # 현재 위치는 X 2 하고
                                matrix[a][j] = 0  # 더해진 숫자는 0으로 바꾸기
                                flag = 0
                                break
                            else:
                                break

    # left
    if command == 'left':
        for i in range(N):
            for j in range(N-1):  # (0 ~ N-2 idx 까지) 마지막줄은 확인할 필요가 없다
                stop = 0
                flag = 1
                if matrix[i][j] == 0:
                    for x in range(j+1, N):
                        stop += matrix[i][x]
                        if stop > 0:  # 땡겨올 숫자가 있으면
                            while matrix[i][j] == 0:  # 0 0 2 가 나올수도 있으니까, 현재 위치에 숫자가 채워질때까지
                                for a in range(j, N-1):  # 0이 나온 줄부터 끝-1줄까지
                                    matrix[i][a] = matrix[i][a+1]  # 한칸위로 땡겨오기
                                    matrix[i][a+1] = 0

                if matrix[i][j] > 0:  # 현재 나의 위치가 숫자라면
                    for a in range(j+1, N):  # 현재 오른쪽부터 마지막줄까지 탐색
                        if flag == 0:  # 한번 끌올 다 하고 멈추기
                            break
                        if matrix[i][a] != 0:  # matrix[i][a]에 숫자가 나오면
                            if matrix[i][j] == matrix[i][a]:   # 숫자가 똑같다면
                                matrix[i][j] *= 2  # 현재 위치는 X 2 하고
                                matrix[i][a] = 0  # 더해진 숫자는 0으로 바꾸기
                                flag = 0
                                break
                            else:
                                break

    # right
    if command == 'right':
        for i in range(N):
            for j in range(N-1, 0, -1):
                stop = 0
                flag = 1

                if matrix[i][j] == 0:
                    for x in range(j-1, -1, -1):
                        stop += matrix[i][x]
                        if stop > 0:  # 땡겨올 숫자가 있으면
                            while matrix[i][j] == 0:  # 0 0 2 가 나올수도 있으니까, 현재 위치에 숫자가 채워질때까지
                                for a in range(j, 0, -1):  # 0이 나온 줄부터 끝-1줄까지
                                    matrix[i][a] = matrix[i][a-1]  # 한칸위로 땡겨오기
                                    matrix[i][a-1] = 0

                if matrix[i][j] > 0:  # 현재 나의 위치가 숫자라면
                    for a in range(j-1, -1, -1):  # 현재 왼쪽부터 첫줄까지 탐색
                        if flag == 0:  # 한번 끌올 다 하고 멈추기
                            break
                        if matrix[i][a] != 0:  # matrix[i][a]에 숫자가 나오면
                            if matrix[i][j] == matrix[i][a]:   # 숫자가 똑같다면
                                matrix[i][j] *= 2  # 현재 위치는 X 2 하고
                                matrix[i][a] = 0  # 더해진 숫자는 0으로 바꾸기
                                flag = 0
                                break
                            else:
                                break

    print('#{}'.format(t))
    n = 0
    while n < N:
        for i in range(N):
            print('{}'.format(matrix[n][i]), end=' ')
        print()
        n += 1