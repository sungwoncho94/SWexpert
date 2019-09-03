T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())  # N = 숫자의 개수, M = 뒤로 보내는 횟수
    n_list = list(map(int, input().split()))

    while M > 0:
        temp = n_list.pop(0)
        n_list.append(temp)
        M -= 1

    print('#{} {}'.format(t, n_list[0]))