T = int(input())

for t in range(1, T+1):
    num_list = []
    board = []
    flag = 1

    # 스도쿠 완성
    for i in range(9):
        num_list = list(map(int, input().split()))
        board.append(num_list)

    # 가로 검증
    for i in range(9):
        check_list = []
        for j in range(9):
            if board[i][j] not in check_list:
                check_list.append(board[i][j])      
        if len(check_list) != 9:
            flag = 0
            break

    if flag == 0 :
        print('#{} 0'.format(t))
        continue

    # 세로 검증
    for j in range(9):
        check_list = []
        for i in range(9):
            if board[i][j] not in check_list:
                check_list.append(board[i][j])
        if len(check_list) != 9:
            flag = 0
            break

    if flag == 0 :
        print('#{} 0'.format(t))
        continue

    # 3*3 검정
    for i in range(0, 7, 3):  # i = 0, 3, 6
        if flag == 0:  # 밑에서 flag가 0 이 되면 거르는 용도
            break
        for j in range(0, 7, 3):
            check_list = []
            for row in range(i, i+3):  # i = 012 / 345 / 678
                for col in range(j, j+3):
                    if board[row][col] not in check_list:
                        check_list.append(board[row][col])
            if len(check_list) != 9:
                flag = 0
                break

    if flag == 1:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))