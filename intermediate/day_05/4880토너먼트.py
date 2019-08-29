def rcp(a, b):
    if a == 1:
        if b == 2:
            return b
        else:
            return a
    elif a == 2:
        if b == 3:
            return b
        else:
            return a
    elif a == 3:
        if b == 1:
            return b
        else:
            return a

T = int(input())

for t in range(1, T+1):
    N = int(input())
    origin_list = list(map(int, input().split()))
    # 1 3 3 3 1 1 3
    temp_list = []
    my_dict = {}
    # index를 같이 관리해야함

    for i in range(N):
        my_dict[i+1] = origin_list[i]
        # {1: 1, 2: 3, 3: 3, 4: 3, 5: 1, 6: 1, 7: 3}

    while len(origin_list) > 1:
        a = origin_list[0]
        b = origin_list[1]
