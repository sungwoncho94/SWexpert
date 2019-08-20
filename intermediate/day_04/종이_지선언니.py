def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result


def find_case(N):
    if N % 20:
        k = N // 20
        l = 1
        result = 1
        while k > 0:
            result += (factorial(k+l)/(factorial(k)*factorial(l))) * 2**k
            k -= 1
            l += 2
    else:
        k = N // 20
        l = 0
        result = 1
        while k > 0:
            result += (factorial(k + l)/(factorial(k) * factorial(l))) * 2 ** k
            k -= 1
            l += 2
    return int(result)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    res = find_case(N)
    print('#{} {}'.format(tc, res))