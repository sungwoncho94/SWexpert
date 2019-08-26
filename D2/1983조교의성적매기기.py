T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    num_of_rank = int(N / 10)
    score_list = []
    rank_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    my_rank = 0

    for n in range(N):
        scores = list(map(int, input().split()))
        result_score = scores[0]*0.35 + scores[1]*0.45 + scores[2]*0.2
        score_list.append((result_score))

    my_score = score_list[K-1]
    for s in score_list:
        if s > my_score:
            my_rank += 1  # my_rank는 실제 등수가 아니라 등수의index임

    real_rank_index = my_rank // num_of_rank
    print('#{} {}'.format(t, rank_list[real_rank_index]))