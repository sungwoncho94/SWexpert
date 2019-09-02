T = int(input())

for t in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    n_list = list(map(int, input().split()))

    for m in range(M):
        idx, num = map(int, input().split())
        left_list = n_list[:idx]
        right_list = n_list[idx:]

        new_list = left_list + [num] + right_list

        n_list = new_list

    print('#{} {}'.format(t, n_list[L]))