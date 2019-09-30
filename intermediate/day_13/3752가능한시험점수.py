'''
문제풀이
(1) 점수 개수 + 1 만큼의 visited list를 만든다
(2) vistied[0] = 1 (0점부터 시작)
(3) 첫번째 점수일 때, 0과 점수가 만들 수 있는 경우의 수 = 0 + 2 --> 0, 2를 visited에 추가
(4) 0, 2와 두번째 점수(=3)이 만들 수 있는 경우의 수 = 0+3, 2+3 --> visited에 추가
.
.
.

'''

T = int(input())

for t in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))

    visited = [0] * (N*100 + 1)
    # 가장 처음 기본점수 = 0부터 시작
    visited[0] = 1

    for score in scores:
        # 한 개의 점수를 돌면서, 현재 점수와 더할 이전 점수들
        sum_list = []

        for v in range(len(visited)):
            # 이전에 만들어진 점수 = v  /  idx = v = 점수
            if visited[v] == 1:
                sum_list.append(v)

        for s in sum_list:
            # 현재점수(=score)와 이전에 존재한 점수들의 합을 visited에 표시하기
            visited[s+score] = 1

    print('#{} {}'.format(t, sum(visited)))