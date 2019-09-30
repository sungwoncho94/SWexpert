import itertools

T = int(input())

for t in range(1, T+1):
    people = int(input())

    total_list = list(map(int, input().split()))

    company = []; home = []
    company.append(total_list[0])
    company.append(total_list[1])
    home.append(total_list[2])
    home.append(total_list[3])

    total_list = total_list[4:]
    
    ctm_x = []
    ctm_y = []
    for x in range(len(total_list)//2):
        ctm_x.append(total_list[2*x])
        ctm_y.append(total_list[(2*x)+1])
    # print(company, home, total_list)  # [0, 0] [100, 100] [70, 40, 30, 10, 10, 5, 90, 70, 50, 20]
    # print(ctm_x)  # [70, 30, 10, 90, 50]
    # print(ctm_y)  # [40, 10, 5, 70, 20]
    num_list = [x for x in range(len(ctm_x))]

    # 자신의 집~random 고객의 집 선택 -> 거리 계산
    min_distance = 99999

    # n번 까지 순서 경우의 수 구하기
    perm_ctm = itertools.permutations(num_list)

    for perm in perm_ctm:  # perm = (0, 1, 2, 3, 4) ... (4, 3, 2, 1, 0)
        distance = 0
        print('순서', perm)
        # (1) 집 ~ 1번 회사 거리
        distance += abs(company[0] - ctm_x[perm.index(0)]) + abs(company[1] - ctm_y[perm.index(0)])
        print(perm.index(0))
        print('회사-집1', ctm_x[perm.index(0)], ctm_y[perm.index(0)])
        
        # (2) 1번집 ~ 마지막집까지 거리
        for i in range(people-1):
            print('집1', ctm_x[perm.index(i)], ctm_y[perm.index(i)], '집2', ctm_x[perm.index(i+1)], ctm_y[perm.index(i+1)])
            distance += abs(ctm_x[perm.index(i)] - ctm_x[perm.index(i+1)]) + abs(ctm_y[perm.index(i)] - ctm_y[perm.index(i+1)])
            if distance >= min_distance:
                break

        # (3) 마지막집 ~ 집 거리
        distance += abs(home[0] - ctm_x[perm.index(4)]) + abs(home[1] - ctm_y[perm.index(4)])
        
        print('거리', distance)

        if distance <= min_distance:
            min_distance = distance
            min_perm = perm

    print(company, ctm_x, ctm_y, home)

    print('#{} {}'.format(t, min_distance))
    print(min_perm)

