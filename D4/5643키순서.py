'''
1
6
6
1 5
3 4
5 4
4 2
4 6
5 2


#1 1
'''

# 플로이드-워셜 알고리즘
# dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
# https://blog.naver.com/ndb796/221234427842

T = int(input())

def printmat(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

for t in range(1, T+1):
    N = int(input())  # 학생들 수
    M = int(input())  # 비교 횟수
    matrix = [[999]*N for i in range(N)]
    # visit = [False] * N+1
    cnt = 0
    
    for m in range(M):
        a, b = map(int, input().split())
        matrix[a-1][b-1] = 1
    # printmat(matrix)

    for i in range(N):
        for j in range(N):
            if i == j:
                matrix[i][j] = 0

    # 1, 2, ...N을 하나씩 선택한 채로, 나머지 숫자 중 2개를 뽑는 알고리즘 필요
    for i in range(N):
        for srt in range(N):
            for tll in range(N):
                # print('i', i, 'short', srt, 'tall', tll)
                if i != srt and srt != tll and i != tll:
                    temp = matrix[srt][i] + matrix[i][tll]
                    if temp < matrix[srt][tll]:
                        matrix[srt][tll] = temp
                        # print('시행')

    # matrix[i][j] or matrix[i][j] 양쪽이 모두 999면 (갈 수 있는 길이 없으면)
    # flag = 0으로 바꾸고 cnt에 아무 값도 더하지 않는다
    for i in range(N):
        flag = 1
        for j in range(N):
            if matrix[i][j] == 999 and matrix[j][i] == 999:
                flag = 0
        if flag == 1:
            cnt += 1


    print('#{} {}'.format(t, cnt))
                
