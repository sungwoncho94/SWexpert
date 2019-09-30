if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        score = list(map(int, input().split()))
        visited = [0]*(N*100+1) # 100개까지 넣음

        visited_len = (N*100+1)
        visited[0] = 1
        for s in score: # 값
            temp = []
            for i in range(visited_len): #
                if visited[i] == 1: # 전단계에서 처리했다면
                    temp.append(i)
            for t in temp:
                visited[t+s] = 1
        print('#%d %d' % (tc, sum(visited)))