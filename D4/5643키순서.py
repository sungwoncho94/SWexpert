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

T = int(input())

def printmat(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

for t in range(1, T+1):
    N = int(input())  # 학생들 수
    M = int(input())  # 비교 횟수
    matrix = [[0]*N for i in range(N)]

    print(matrix)
    # for m in range(M):
    #     a, b = map(int, input().split())