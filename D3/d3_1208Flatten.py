T = 10  # 총 10개의 test case

for t in range(1, T+1):
    dump = int(input())  # dump할 수 있는 횟수  (0이 될때까지)
    box_list = list(map(int, input().split()))

    for d in range(1, dump+1):  # dump가 진행될 때 마다 1씩 빼고, 0이 되면 정지
        max_box = max(box_list)
        min_box = min(box_list)

        # max, min box의 인덱스번호 출력
        # print(box_list.index(max_box), box_list.index(min_box))
        # 자동으로 가장 앞번호부터 출력됨

        # 가장 큰 박스 -1 / 가장 작은 박스 + 1
        box_list[box_list.index(max_box)] = max_box -1
        box_list[box_list.index(min_box)] = min_box + 1
        d -= 1
    print(f'#{t} {max(box_list) - min(box_list)}')
