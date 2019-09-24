import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    task = [list(map(int, input().split())) for i in range(N)] # [i][0]start, [i][1]end
    task.sort(key=lambda x : x[1])

    ans = pre_end = 0
    for i in range(N):
        if pre_end <= task[i][0]:
            ans += 1
            pre_end = task[i][1]

    print("#%d" % tc, ans)