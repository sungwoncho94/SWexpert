'''
1. i, j의 범위가 matrix내부인지 판단
2. 위에서 방문한 j를 다시 방문할 수 없음 (i는 계속 한줄씩 내려오니까 판단 안해도 된다)
3. matrix[x][y]의 합을 구하면서 최소값 갱신
4. sum(matrix[x][y]) >= min이면 탐색X (가지치기)
'''
def search(i):
    global min_result, temp
    # 가지치기
    if temp > min_result:
        return

    # 모든 경로를 다 돌았다면 확인
    if i == N:
        if min_result >= temp:
            min_result = temp
        return

    # 0~N-2까지 시행할 알고리즘  /  연산
    for j in range(N):
        if j_visited[j] == 0:
            j_visited[j] = 1
            temp += matrix[i][j]
            search(i+1)
            # 위 노드로 갈 수 있도록 초기화
            temp -= matrix[i][j]
            j_visited[j] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = []

    for n in range(N):
        m_list = list(map(int, input().split()))
        matrix.append(m_list)

    min_result = 99999
    temp = 0

    # search 함수 안에서 만들면 재귀 들어갈 때마다 계속 초기화됨
    j_visited = [0] * N
    search(0)
    print('#{} {}'.format(t, min_result))
    