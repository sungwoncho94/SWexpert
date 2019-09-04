import sys
sys.stdin = open("5102.txt", "r")

def search_path(start_node):
    global result
    que.append(start_node) #방문할 노드에 시작 노드를 저장
    visited[start_node] = 1

    while que: #방문할 노드가 빌때까지 반복
        start_node = que.pop(0) #방문할 노드에서 첫번째 삭제
        for next_node in range(1, v+1): #방문할 노드에 연결된 노드를 차례대로 시도
            #연결된 노드가 방문하지 않은 노드이면
            if MyMap[start_node][next_node] and not visited[next_node]:
                que.append(next_node) #방문할 노드에 추가
                visited[next_node] = 1 #방문한 노드로 등록
                #거리저장소에 현재노드에 등록된 거리+1을 방문할 노드에 저장
                distance[next_node] = distance[start_node] +1
                if next_node == end_node: #방문할 노드가 끝노드이면  방문할 노드값을 결과에 저장하고 종료
                    result = distance[next_node]
                    return
    return

TC = int(input())
for tc in range(1, TC+1):
    v,e = map(int, input().split())
    MyMap = [[0] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    distance = [0] * (v+1) #시작노드와의 거리 저장용

    for i in range(e):
        start, end = map(int, input().split())
        MyMap[start][end] = 1  #방향성이 없으니 양쪽에서 연결하도록
        MyMap[end][start] = 1

    start_node, end_node = map(int, input().split())

    que = []  #방문할 노드목록
    result = 0
    search_path(start_node)
    print('#{} {}'.format(tc,result))