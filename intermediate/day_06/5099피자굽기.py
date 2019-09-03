T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())  # N = 화덕 수, M = 피자 수

    pizza_list = list(map(int, input().split()))
    n_list = []

    for n in range(N):
        n_list.append(pizza_list[n])  # 처음에 화덕 개수만큼 들어갈 것
    
    while