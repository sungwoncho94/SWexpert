T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())  # N = 화덕 수, M = 피자 수

    p_list = list(map(int, input().split()))
    Q = [0] * N  # 화덕 수
    idx_list = [0] * N  # idx 표시할 list
    cnt = 0
    flag = 1

    # cheese = 화덕에 넣을 pizza의 idx -> M이 기준이다
    # 화덕 수만큼 for문을 돌면서 화덕에 피자를 채운다.
    for cheese in range(N):
        Q[cheese] = p_list[N-cheese-1]
        idx_list[cheese] = N-cheese-1

    # 한 번 회전 = n-1 idx -> 0 idx
    while flag == 1:
        # n-1 idx에 오면 치즈를 절반 녹여서 0 idx로 보낸다
        target = Q[-1] // 2
        Q.insert(0, target)
        Q.pop()

        # 만약 치즈의 양이 0이 되면, 다음 피자를 가지고온다.
        if Q[0] == 0:
            # 가져올 피자가 있다면,
            if cheese < M-1:
                cheese += 1
                # 다음 피자를 오븐에 넣고
                Q[0] = p_list[cheese]
                # 가져온 피자의 idx + 1을 idx_list에 넣어줌
                idx_list.insert(0, idx_list[-1])
                idx_list.pop()
                idx_list[0] = cheese

            else: # 가져올 피자가 없다면, idx_list에 0만 넣기
                idx_list.insert(0, 0)
                idx_list.pop()
        # 치즈의 양이 0이 아니라면 -> 계속 회전
        else:
            # 마지막 idx에 있던 피자를 0번으로 옮긴다
            idx_list.insert(0, idx_list[-1])
            idx_list.pop()
        
        #print('피자', Q, 'idx', idx_list, cheese)

        # 마지막 피자까지 오븐에 넣은 상태이고, 오븐에 피자가 하나만 남았다면
        if cheese == M-1:
            if Q.count(0) == N-1:
                flag = 0

    #print(idx_list)
    print('#{} {}'.format(t, sum(idx_list)+1))
