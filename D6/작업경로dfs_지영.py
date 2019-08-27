T = 10
for tc in range(1, T+1):
    def dfs(v): 
        stack=[]; path=''
        stack.append(v)

        while stack: 
            for i in range(len(stack)) :
                pop_v = stack.pop()
                if visited[pop_v] > 0:
                    visited[pop_v] -= 1
                if visited[pop_v] == 0:
                    visited[pop_v] = 'FIN'
                    path += str(pop_v)
                    path += ' '
                    stack.extend(adj_l[pop_v])
        return path

    # adj = [[], [2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]
    # visit = [0, fin, fin, fin, fin, 1, 1, fin, 0, 1]
    if __name__=="__main__":
        V, E = map(int, input().split()) 
        l = list(map(int, input().split()))
        start = [l[i] for i in range(E * 2) if not i % 2]
        end = [l[i] for i in range(E * 2) if i % 2]

        adj_l = [[] for i in range(V+1)]
        for idx in range(0, V+1):
            for j in start:
                if idx == j:
                    temp = start.index(j)
                    start[temp] = 0
                    adj_l[idx].extend([end[temp]])
        print(adj_l)

        visited = [0 for i in range(V + 1)]
        for idx in range(0, V+1):
            visited[idx] = end.count(idx)

        dfs_v=''
        for i in range(1, V+1):
            if visited[i] == 0:
                dfs_v += dfs(i)
        print('#%d %s' % (tc, dfs_v))