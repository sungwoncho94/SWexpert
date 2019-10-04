# BFS / Q사용해서 풀어보기

def BFS(n):


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    visit = [0] * (N+1)

    start_end = [[] for i in range(M)]
    

