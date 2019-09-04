import sys
sys.stdin = open("4880.txt", "r")

def battle(card_no1, card_no2):
    if data[card_no1]==data[card_no2]:#카드번호가 작으면 승
        if card_no1 < card_no2:
            return card_no1
        return card_no2
    if data[card_no1]==1: #가위
        if data[card_no2]==2:#바위
            return card_no2
        else:
            return card_no1
    if data[card_no1]==2: #바위
        if data[card_no2]==3:#보
            return card_no2
        else:
            return card_no1
    if data[card_no1]==3: #보
        if data[card_no2]==1:#가위
            return card_no2
        else:
            return card_no1

def mydiv(start, end): #순서번호 입력
    #종료
    if start == end: #한장으로 나눠진 경우
        return start
    p = (start+end)//2 #반 나누는 기준 번호
    card_no1 = mydiv(start,p) #한장까지 분할. 카드의 번호 반환
    card_no2 = mydiv(p+1,end) #한장까지 분할. 카드의 번호 반환
    winner_card_no = battle(card_no1, card_no2)
    return winner_card_no #승자카드번호 반환

TC = int(input()) #테스트 횟수

for tc in range(1, TC+1):
    n = int(input()) #게임참여숫자 갯수
    data = list( map(int,input().split()) )  # 게임참여숫자목록
    winner = mydiv(0,n-1)
    print("#%d %d" % (tc, winner+1))