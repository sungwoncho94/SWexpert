'''
2
20 12
76 58 78
96 100 99
97 99 98
96 100 98
98 97 100
57 67 77
75 99 63
84 81 79
99 99 98
85 74 88
87 98 85
85 80 73
92 79 75
79 93 93
94 83 94
99 99 99
55 94 71
90 89 77
98 100 98
98 99 98
40 18
69 71 57
92 83 95
100 97 100
97 96 99
98 94 89
53 84 83
80 96 81
100 96 98
100 75 100
69 62 90
99 63 66
66 99 94
98 78 73
97 95 91
86 85 89
76 85 90
98 96 96
94 96 100
62 60 84
70 79 70
97 98 90
94 98 100
75 95 82
94 56 65
80 90 90
97 97 100
93 86 79
93 96 87
100 93 93
79 90 79
88 77 95
73 83 91
72 57 84
95 99 91
86 75 100
100 69 56
85 99 97
100 96 100
98 99 98
79 96 91
'''

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
    print(score_list)
    print(my_score, my_rank, real_rank_index)
    print('#{} {}'.format(t, rank_li*^^st[real_rank_index]))