T = int(input())

for t in range(1, T+1):
    N = int(input())
    nasa_list = list(map(int, input().split()))
    nasa=[f'#{t}']
    first_size = nasa_list[::2]
    last_size = nasa_list[1::2]

    # 처음 오는 나사 정하기
    for i in range(len(first_size)):
        if first_size[i] not in last_size:
            idx = i
    # idx = 현재 나사의 index

    # 첫번째 나사의 앞,뒤 크기 리스트 설정
    nasa.append(first_size[idx])
    nasa.append(last_size[idx])

    while len(nasa) < len(nasa_list):
        for i in range(len(last_size)):
            # 원래 정해졌던 첫나사end size == 새로 올 두번째 나사 첫 size
            if last_size[idx] == first_size[i]:
                idx2 = i  # 두번째 나사 idx설정

                # 두번째 나사 앞뒤크기 설정
                nasa.append(first_size[idx2])
                nasa.append(last_size[idx2])

                # idx2 = 1과 같은 문단에 적어야 error나지 않는다.
                last_size[idx] = last_size[idx2]
                continue

    for n in nasa:
        print(n, end=' ')
    print()