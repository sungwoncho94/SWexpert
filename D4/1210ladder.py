T = 10
 
for t in range(1, T+1):
    N = int(input())
    # matrix 완성
    matrix = []
    for i in range(100):
        m_list = list(map(int, input().split()))
        matrix.append(m_list)
 
    # 도착점 찾기  (예시1 - 99, 57)
    row = 99
    for col in range(100):
        if matrix[row][col] != 2:
            col -=1
        else:
            break
    row = 98
    '''
    # y좌표 왼쪽이동, 오른쪽 이동
    # 위로 가는 사다리가 나오기전까지 계속 한쪽 방향으로 이동
    dy = [-1, 1]  
    '''
    while row > 0:  # row = 0이 될 때 까지 돌린다
        # 마지막 줄에서 양옆으로 이동하는 경우는 없기 때문에, row = 98에서 시작
        # location = matrix[row][col] = matrix[98][57]
        # print(row, col)
 
        if col == 99:  # col index가 양 끝인 경우
            # 왼쪽으로 가야하는 경우부터
            if matrix[row][col-1] == 1:
                matrix[row][col] = 0  # 현재 위치를 0으로 바꾸고 이동
                col -= 1
            else:  # 위로 가야하는 경우
                matrix[row][col] = 0
                row -= 1
        elif col == 0:
            if matrix[row][col+1] == 1:
                matrix[row][col] = 0
                col += 1
            else:
                matrix[row][col] = 0
                row -= 1
        else:  # col index가 양 끝이 아닌 경우
            # 좌, 우 이동부터 살피고 없으면 위로 이동한다.
            # 좌, 우로 이동할때는 위로 가는 사다리가 나오기 전까지 한 방향으로 이동
            if matrix[row][col-1] == 1:  # 왼쪽으로 가는 사다리가 있으면,
                # col이 이미 0이 된 경우는 돌리면 안대
                while matrix[row][col-1] == 1:
                    matrix[row][col] = 0
                    col -= 1
                    if col == 0:
                        break
 
            elif matrix[row][col+1] == 1:
                # col이 이미 99인 경우는 돌리면 안대
                while matrix[row][col+1] == 1:
                    matrix[row][col] = 0
                    col += 1
                    if col == 99:
                        break
                   # location = matrix[row][col]
            else:  # 좌, 우에 1이 나올때 까지 위로 이동
                while matrix[row][col-1] == 0 and matrix[row][col+1] == 0:
                    matrix[row][col] = 0
                    row -= 1
 
 
    print('#{} {}'.format(N, col))