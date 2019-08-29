def mydiv(start, end):
    if start == end:
        return start

    p = (start + end) // 2  # 학생을 반 나누는 기준번호
    card_num1 = mydiv(start, p)  # 한장까지 분할, 카드의 번호가 반환
    card_num2 = mydiv(p+1, end)
    win_num = battle(card_num1, card_num2)
    return win_num

def battle(a, b):
    if data[a] == data[b]:
        if a < b:
            return a
        return b
    if data[a] == 1:
        if data[b] == 2:
            return b
        else:
            return a
    if data[a] == 2:
        if data[b] == 3:
            return b
        else:
            return a
    if data[a] == 3:
        if data[b] == 1:
            return b
        else:
            return a


T = int(input())

for t in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    winner = mydiv(0, n-1)
    print('#{} {}'.format(t, winner))
