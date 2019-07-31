
T = int(input())

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
    result_list = []
    for n in range(0, N - M + 1):  # 긴단어의 시작 범위  (0, 1, 2)
        sum_result = 0
        for m in range(M):  # 짧은 단어의 길이만큼 더한다 (m=3, 3칸)
            num = N_list[n+m]
            sum_result += num
        result_list.append(sum_result)

    max_num = max(result_list)
    min_num = min(result_list)

    print(f'#{t} {max_num - min_num}')