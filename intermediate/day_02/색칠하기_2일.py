T = int(input())

# N = 3일 때 함수부터 만들어보자.
for t in range(1, T+1):
    N = int(input())
    temp = []; red_list = []; blue_list = []
    x_result = []; y_result = []; result_x = result_y = 0; result = 0

    for n in range(N):
        x_list = []
        y_list = []
        temp_list = []
        temp = list(map(int, input().split()))
        # (1 4 8 5 1)

        for x in range(temp[0], temp[2]+1):
            # range(1, 8+1)
            if x not in x_list:
                x_list.append(x)
                # [1, 2, 3, 4, 5, 6, 7, 8]
                
        for y in range(temp[1], temp[3]+1):
            if y not in y_list:
                y_list.append(y)
                # [4, 5]

        # 빨간사각형, 파란사각형 나누기
        if temp[4] == 1:
            temp_list.append(x_list)
            temp_list.append(y_list)
            red_list.append(temp_list)
        else:
            temp_list.append(x_list)
            temp_list.append(y_list)
            blue_list.append(temp_list)
    # red_list = [[[1, 2, 3, 4, 5, 6, 7, 8], [4, 5]], [[1, 2, 3], [8, 9]]]
    # blue_list = [[[3, 4, 5], [2, 3, 4, 5, 6, 7, 8]]]
    
    for red in red_list:
        for blue in blue_list:
            for r in red[0]:
                if r in blue[0]:
                    result_x += 1
            x_result.append(result_x)
            result_x = 0

    for red in red_list:
        for blue in blue_list:
            for r in red[1]:
                if r in blue[1]:
                    result_y += 1
            y_result.append(result_y)
            result_y = 0
    
    # x_result = [3, 1]
    # y_result = [2, 1]
    
    for i in range(len(y_result)):
        result += x_result[i] * y_result[i]

    print(f'#{t} {result}')
