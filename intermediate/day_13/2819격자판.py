'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1

#1 23
'''

def iswall(x, y):
    if x < 0 or x > 3 or y < 0 or y > 3:
        return False
    else:
        return True


def DFS(x, y, cnt):
    global result_list, temp, result_cnt

    # 현재 위치에서 시행할 동작들
    if iswall(x, y) == False:
        return

    temp += matrix[x][y]
    
    if cnt == 7:
        if temp not in result_list:
            result_list.append(temp)
            result_cnt += 1
        # depth == 7에서 위로 올라갈 때
        temp = temp[:6]
        return

    # 밑에 4개 노드에 대해서 시행할 동작들
    for i in range(4):
        
        x += dx[i]
        y += dy[i]
        cnt += 1

        DFS(x, y, cnt)

        x -= dx[i]
        y -= dy[i]
        cnt -= 1

    # 7미만 노드에서 더 위로 올라갈 떄,
    temp = temp[:len(temp)-1]


T = int(input())

for t in range(1, T+1):
    matrix = []
    result_list = []  # 만들어진 7자리 숫자를 넣을 list
    result_cnt = 0
    temp = ''

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # matrix 완성
    for m in range(4):
        m_list = list(map(str, input().split()))
        matrix.append(m_list)
    
    for i in range(4):
        for j in range(4):
            DFS(i, j, 1)
            # print(result_list)

    print('#{} {}'.format(t, result_cnt))
