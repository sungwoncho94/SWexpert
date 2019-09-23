import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort()
    truck.sort()

    ans = 0
    while len(weight) and len(truck):
        tt = truck.pop()
        while len(weight):
            tw = weight.pop()
            if tw <= tt:
                ans += tw
                break

    print("#%d" % tc, ans)