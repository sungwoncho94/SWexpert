T = int(input())

for t in range(1, T+1):
    num_list = list(map(int, input().split()))
    num_list.sort()
    # .sort() 는 리스트 자체를 바꿔버린다. 뒤에 ()있어야함

    # del함수 사용방법 = del list[idx]
    del num_list[0]
    num_list.pop()

    result = sum(num_list) / len(num_list)
    print('#{} {}'.format(t, round(result)))
    # round(올림)함수 = round(n, 남길 소수점)