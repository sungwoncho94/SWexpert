'''
완전중요! 그림그리면서 처음부터 끝까지 손으로 따라가보기
'''

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[0] * 8 for in range(8)]

# 양방향 그래프로 표현하기 
# -> 실제 그래프는 무방향이기때문에 몇번부터 시작하던 상관없음
for i in range(0, len(edges), 2):
    G[edges[i]][edges[i+1]] = 1
    G[edges[i+1]][edges[i]] = 1

def dfs(v):
    visited = [0] * 8  # 한 번 방문한곳은 방문하지 않도록
    stack = [0] * 10  # 조회할 숫자들을 쌓아놓는 스택
    top = -1

    top += 1  # push 연산 = top을 하나 증가시켜서 그 위치에 값 삽입
    stack[top] = v

    while top != -1:  # top이 -1이면 초기값임 == 비어있는 상태임
        v = stack[top]
        top -= 1
        # 자기처리
        if visited[v] != 1:
            visited[v] = 1
            print(v)
            
            # 이웃 처리
            for i in range(1, 8):
                # 나와 연결선이 있는지 & 방문한 적이 있는지 조회
                if G[v][i] and not visited[i]:
                    top += 1
                    stack[top] = i

                
# 재귀로 작성
def dfsr(v):
    print(v)
    visited[v] = True

    for i in range(1, 8):
        if G[v][i] and not visited[i]:
            dfsr(i)