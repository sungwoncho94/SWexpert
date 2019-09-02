T = int(input())

for t in range(1, T+1):
    # N = 수열의 길이, M = 수열의 개수
    N, M = map(int, input().split())

    origin_list = list(map(int, input().split()))
    result = []

    for m in range(M-1):  # list 2, 3, 4를 받는다
        input_list = list(map(int, input().split()))
        
        for n in range(len(origin_list)):
            if origin_list[n] > input_list[0]:
                origin_list[n:0] = input_list
                break
            if n == len(origin_list)-1:
                origin_list += input_list

    for i in range(10):
        result.append(origin_list[-i - 1])

    print('#{} {}'.format(t, ' '.join(list(map(str, result)))))

