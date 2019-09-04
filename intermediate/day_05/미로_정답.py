import sys
sys.stdin = open("4875.txt", "r")

def is_ok(y,x):  #해당 좌표가 이동가능한지 여부
    return 0<=y<n and 0<=x<n and mymap[y][x] != 1

def find_map(startY,startX):  #재귀함수
    global result
    # 1. 종료조건
    if mymap[startY][startX]==3:
        result=1
        return #검색 종료
    # 2. 반복검색
    # 4방향 검색

    visited.append( (startY,startX) )
    if is_ok(startY, startX + 1) and (startY,startX+1) not in visited:
        find_map(startY, startX + 1) #우측
    if result==0 and is_ok(startY +1, startX) and (startY,startX+1) not in visited:
        find_map(startY +1, startX )  #아래
    if result==0 and is_ok(startY, startX - 1) and (startY, startX - 1) not in visited:
        find_map(startY, startX - 1)  #좌측
    if result==0 and is_ok(startY - 1, startX) and (startY - 1, startX) not in visited:
        find_map(startY - 1, startX)  #위



TC = int(input()) #테스트 횟수

for tc in range(1, TC+1):
    n = int(input()) #한변의 길이
    mymap = [ ] # 지도정보
    for i in range(n):
        l = list( input() )
        row_list = list(map(int, l))
        mymap.append(row_list)
    #print("mymap", mymap)
    # 시작지점 찾기
    startX=-1
    startY=-1
    for y in range(n) :
        for x in range(n) :
            if mymap[y][x]==2:
                startX,startY = x,y
    # 미로 -> 방문했던 위치 저장소
    visited = []
    result = 0  #목적지 도착 여부
    find_map(startY,startX)
    print("#%s %s"%(tc,result))

