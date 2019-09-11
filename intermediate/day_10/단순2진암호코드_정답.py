T = int(input())

secret_code = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]

# 단순히 앞자리부터 7자리씩 끊어읽는 방법
for t in range(1, T+1):
    N, M = map(int, input().split())
    code_list = []
    cnt = 0
    trans_list = []

    for n in range(N):
        arr = list(map(int, input()))
        
    t = 0
    for i in range(len(arr)):
        t = t*2 + int(arr[i])
        if (i+1) % 7 == 0:
            print(t, end=' ')
            t = 0

