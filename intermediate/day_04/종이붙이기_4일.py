def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

# T = int(input())

# for t in range(1, T+1):
# 홀수일 때
for N in range(10, 301, 10):
    result = 0
    B = int(N // 20)  # 큰 네모 개수
    for b in range(B+1):
        s = int((N/10) - (2*b))
        result += int((factorial(b+s) / (factorial(b) * factorial(s))) * 2**b)



    print('#{} {}'.format(N, result))