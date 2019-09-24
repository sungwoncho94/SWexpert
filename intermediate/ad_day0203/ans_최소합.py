import sys
sys.stdin = open("input.txt", "r")

def solve( x, y, sum ):
    global ans
    global cnt
    cnt += 1

    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if x == N - 1 and y == N - 1:
        if ans > sum + mat[x][y]:
            ans = sum + mat[x][y]
    else:
        # if sum + mat[x][y] < ans:
            solve(x + 1, y, sum + mat[x][y])
            solve(x, y + 1, sum + mat[x][y])


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())

    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))

    ans = 300
    cnt = 0

    solve(0, 0, 0)
    print("#%d" % tc, ans, cnt)