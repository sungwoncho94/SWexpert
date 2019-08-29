def find_min(row):
    global temp, min_num

    if temp > min_num:
        return  # 누적중인 값이 최소값보다 크면 하위검색 중단
    
    if row == n:  # row가 맨 아래까지 내려오면,
        if temp < min_num:  # 누적값이 최소값보다 작으면 최소값 갱신
            min_num = temp
        return

    for x in range(n):
        if visited[x] == 0:
            visited[x] = 1
            temp += matrix[row][x]  # 최소값 누적변수에 누적
            find_min(row+1)
            visited[x] = 0
            temp -= matrix[row][x]  # 들어갔다 나왔으니 누적숫자만큼 뺀다


T = int(input())
for t in range(1, T+1):
    N = int(input())  # 한변의 길이
    visited = [0 * n]
    min_num = 99999  # 최소값 저장용
    temp = 0  # 중간 열별 값 저장용. 최소값보다 작으면 최소값에 저장
    matrix = []
    # matrix = [list(map(int, input().split())) for i in range(N)]
    for n in range(N):
        m_list = list(map(int, input().split()))
        matrix.append(m_list)
    
    find_min(0)
    print('#{} {}'.format(t, min_num))
