import sys
sys.stdin = open("5105.txt", "r")

def isOK(y, x):
    #y,x좌표가 영역내에있고
    return 0 <= y < N and 0<= x < N and (mymap[y][x] == 0 or mymap[y][x] == 3)

def search_map(start_y, start_x):
    global result_distance
    que.append((start_y, start_x)) #출발좌표를 방문할 큐에 저장
    visited.append((start_y, start_x)) #방문이력 좌표에 방문좌표등록

    while que: #방문할 큐가 빌 때까지
        start_y, start_x = que.pop(0) #방문할 좌표 큐 맨앞 삭제. 지금 좌표
        for dir in range(4):  #4방향에서 갈수있는 좌표 검사
            next_y = start_y + dy[dir] #현재방향에서 다음 좌표를 생성
            next_x = start_x + dx[dir]
            # 다음좌표가 갈 수있고 방문이력이 없으면
            if isOK(next_y, next_x) and (next_y, next_x) not in visited:
                que.append((next_y, next_x)) #방문할 좌표큐에 저장
                visited.append((next_y, next_x)) #방문한 좌표에 등록
                distance[next_y][next_x] = distance[start_y][start_x] + 1
                if mymap[next_y][next_x] == 3:
                    result_distance = distance[next_y][next_x] - 1
                    return
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    mymap = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for y in range(N): #시작좌표찾기
        for x in range(N):
            if mymap[y][x] == 2: #값이 2이면 시작좌표임.
                start_y, start_x = y, x

    dy = [1, -1, 0, 0] #4방향에 대한 x,y증감값 정의  상,하,좌,우
    dx = [0, 0, -1, 1] #4방향에 대한 x,y증감값 정의

    result_distance = 0
    que = []
    distance = [[0] * N for _ in range(N)]
    search_map(start_y, start_x) #길찾기 시작
    print(f'#{tc} {result_distance}')