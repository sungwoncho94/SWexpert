def get_result(x, y):
    global result, sub_result

    if sub_result > result:
        return

    if 0 not in visited:
        sub_result += abs(x - Home_x) + abs(y - Home_y)
        if result > sub_result:
            result = sub_result
        sub_result -= abs(x - Home_x) + abs(y - Home_y)
        return

    for i in range(N):
        x1 = customer[i][0]
        y1 = customer[i][1]
        if not visited[i]:
            visited[i] = 1
            sub_result += abs(x - x1) + abs(y - y1)
            get_result(x1, y1)
            visited[i] = 0
            sub_result -= abs(x - x1) + abs(y - y1)


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Data = list(map(int, input().split()))
    Office_x, Office_y = Data[0], Data[1]
    Home_x, Home_y = Data[2], Data[3]
    # print(Data)

    customer = []
    for i in range(2, N + 2):
        x = Data[i * 2]
        y = Data[i * 2 + 1]
        customer.append([x, y])

    # print(customer)

    visited = [0] * N
    sub_result = 0
    result = 987654321
    get_result(Office_x, Office_y)
    print('#%d %d' % (tc, result))