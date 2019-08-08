T = int(input())

for t in range(1, T+1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a = len(A)
    N, K = map(int, input().split())
    subset = []
    result = []

    for i in range(1<<a):
        subset += [[A[j] for j in range(a) if i & (1 <<j)]]
    '''
    for i in range(1<<a):2^a 개의 부분집합이 생긴다.
        for j in range(a):  # 각 원소마다 bit비교(원소의개수만큼 bit비교)
            if i & (1<<j):  # 1<=i<=2^a 의 bit와 j를 비교해서, i와 j가 같으면 출력
                subset += [A[j]
    이건 왜 안될까??
    '''
    
    for i in subset:
        if len(i) == N and sum(i) == K:
            result.append(i)
    
    print(f'#{t} {len(result)}')