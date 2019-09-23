import sys
sys.stdin = open("input.txt", "r")


def solve(k):
    global ans
    if k == N - 1:
        tsum = mat[0][perm[0]]
        for i in range(len(perm) - 1):
            tsum += mat[perm[i]][perm[i + 1]]
        tsum += mat[perm[N - 2]][0]
        if ans > tsum :
            ans = tsum
    else:
        for i in range(1, N):
            if not visited[i]:
                visited[i] = 1
                perm[k] = i
                solve(k + 1)
                visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())

    mat = [list(map(int, input().split())) for i in range(N)]

    ans = 987654321

    perm = [0] * (N - 1)
    visited = [0] * N
    solve(0)
    print("#%d" % tc, ans)