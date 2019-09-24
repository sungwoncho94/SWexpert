def backtaracking(location):
    global temp_cnt, min_charge

    # 제한시간초과 -> 가지치기 해주기
    if temp_cnt >= min_charge:
        return

    # 현재 위치 = location, 끝에서부터 역으로 jump해보기
    for jump in range(station_list[location], 0, -1):

        # 내가 jump한 위치
        location += jump
        temp_cnt += 1

        # 정류장에 도착하거나, 그 이상을 갈 수 있다면 min_cahrge 입력
        if location >= N-1:
            if temp_cnt < min_charge:
                min_charge = temp_cnt
            # 도착점에 도달했으니, 다시 앞상태로 돌아가야함
            location -= jump
            temp_cnt -= 1
            # continue -> for 문으로 돌아가서 jump-1만큼 jump
            continue
        # 도착점에 도달하지 못했다면, 계속 backtracking해서 밑으로 들어가게 해야함
        backtaracking(location)
        # 이해가 안된다면 일단 외워야한다
        # 도착점까지 도달하지 못한 상태에서 상위 location으로 돌려주는 코드
        temp_cnt -= 1
        location -= jump
        

T = int(input())

for t in range(1, T+1):
    N_list = list(map(int, input().split()))

    N = N_list[0]
    station_list = N_list[1:]  # [2, 3, 1, 1]

    # 최소 충전횟수
    min_charge = 999
    # 임시 cnt는 여기서 선언해야함
    temp_cnt = 0

    start_location = 0  # 시작노드 = 1 / location = 0

    backtaracking(start_location)

    print('#{} {}'.format(t, min_charge-1))

