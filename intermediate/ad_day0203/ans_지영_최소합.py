def notwall(new_x, new_y): 
    if 0<=new_x<N and 0<=new_y<N:
        return True
    return False
​
def DFS(x, y):
    global subresult, result
​
    if result < subresult:
        return
​
    if x == N-1 and y == N-1: #마지막 위치에 오면
        result = subresult #앞에서 제어를 했어야
        return
​
    for j in range(2):  # 오른쪽 혹은 아래쪽으로 움직인 이후에
        new_x = x + dir_x[j]
        new_y = y + dir_y[j]
        if notwall(new_x, new_y) and (new_x, new_y) not in visited:
            visited.append((new_x, new_y))
            subresult += arr[new_x][new_y]
            DFS(new_x, new_y)
            visited.remove((new_x, new_y))
            subresult -= arr[new_x][new_y]
​
​
if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        arr = [0]*N
        for i in range(N):
            arr[i] = list(map(int, input().split()))
​
        visited = []
        result, subresult = 9999999, arr[0][0]  # 왜 이렇게 초기화?
        dir_x = [0, 1]; dir_y =[1, 0] 
        DFS(0, 0) 
        print('#%d %d' % (tc,result))