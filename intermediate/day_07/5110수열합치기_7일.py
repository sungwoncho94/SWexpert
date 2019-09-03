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
<<<<<<< HEAD
                origin_list[n:n] = input_list
=======
                origin_list[n:0] = input_list
>>>>>>> c484acf708ed7d6f5af074afa4e0790e10b73832
                break
            if n == len(origin_list)-1:
                origin_list += input_list

    for i in range(10):
        result.append(origin_list[-i - 1])

    print('#{} {}'.format(t, ' '.join(list(map(str, result)))))

