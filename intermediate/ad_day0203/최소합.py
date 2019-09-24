# 완전탐색 & 가지치기 방법

def solve(x, y, sum):
    # solve 할 때 마다 계산 cnt + 1
    cnt += 1

    # 범위를 넘어가면 끝냄
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    



T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = []

    for n in range(N):
        n_list = list(map(int, input().split()))
        matrix.append(n_list)

    answer = 9999
    cnt = 0

    solve(0, 0, 0)

