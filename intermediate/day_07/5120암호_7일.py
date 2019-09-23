T = int(input())

for t in range(1, T+1):
    # N = 시작배열의 수 / M = M칸 추가 / K = K번 반복
    N, M, K = map(int, input().split())
    n_list = list(map(int, input().split()))
    idx = 0
    result = []

    for k in range(K):
        idx += M
        if idx > len(n_list):
            idx -= len(n_list)
        
        n_list[idx:0] = [0]d
        if idx < len(n_list) - 1:
            n_list[idx] = n_list[idx-1] + n_list[idx+1]
        elif idx == len(n_list) - 1:
            n_list[idx] = n_list[idx - 1] + n_list[0]

    if len(n_list) <= 10:
        for i in range(len(n_list)):
            result.append(n_list[-i - 1])
    else:
        for i in range(10):
            result.append(n_list[-i - 1])

    print('#{} {}'.format(t, ' '.join(list(map(str, result)))))