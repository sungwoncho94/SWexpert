def game(left, right, k):
    if left < right:
        return 0
​
    if k == N:
        return 1
​
    res = 0
    for idx in range(N):
        if visit[idx]:
            continue
        else:
            visit[idx] = True
            res += game(left+weight[idx], right, k+1)
            # for문을 여러번 돌기 때문에, 마지막 값만 저장이 됨 -> res에 저장하면서 진행해야함.
            res += game(left, right+weight[idx], k+1)
            visit[idx] = False
    return res  # l+r은 전체 경우의 수
​
​
​
for t in range(int(input())):
    N = int(input())
    weight = list(map(int, input().split()))
    visit = [False] * N  
​
    cnt = game(0, 0, 0)
​
    print(cnt)