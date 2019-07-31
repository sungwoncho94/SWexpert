T = int(input())
matrix = []

# 일렬로 표시되었지만, 매트리스라고 생각하고 풀어보자.
for t in range(1, T+1):
    N, K = map(int, input().split())
    for n in range(N):
        list_n = list(map(int, input().split()))  # a0 ~ aN-1 까지
        matrix.append(list_n)
        print(f'{n} {list_n} {matrix}')

    count = 0 # result

    for l in range(N):
        for i in range(N-K+1):
            print(l, i)
            print(matrix[l][i] + matrix[l][i+1] + matrix[l][i+2])
           # if sum(matrix[l][i] + matrix[l][i+1] + matrix[l][i+2]) == 3:
