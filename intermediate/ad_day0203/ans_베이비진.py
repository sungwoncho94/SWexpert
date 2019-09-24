import sys
sys.stdin = open("input.txt", "r")

def runchk(card):
    for i in range(8):
        if card[i] >= 1 and card[i+1] >= 1 and card[i+2] >= 1:
            return True

def game():
    card1 = [0 for i in range(10)]
    card2 = [0 for i in range(10)]
    for i in range(12):
        n = lst[i]
        if i % 2  == 0:
            card1[n] += 1
            if card1[n] == 3:
                return 1
            if runchk(card1):
                return 1
        else:
            card2[n] += 1
            if card2[n] == 3:
                return 2
            if runchk(card2):
                return 2
    return 0


TC = int(input())
for tc in range(1, TC + 1):
    lst = list(map(int, input().split()))

    print("#%d" % tc, game())