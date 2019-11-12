'''
1
6
6
1 5
3 4
5 4
4 2
4 6
5 2


#1 1
'''
T = int(input())

for t in range(1, T+1):
    result = []
    cnt = 0
    length_list = []
    N = int(input())  # 학생들 수
    M = int(input())  # 비교 횟수
    for m in range(M):
        a, b = map(int, input().split())
        length_list.append([a, b])
        if len(length_list) != 0:
            for l_list in length_list:
                if a == l_list[-1]:
                    new_list = []
                    new_list = l_list
                    new_list.append(b)
                    length_list.append(new_list)
        else:
            length_list.append([a, b])

        # print(length_list)
    for i in range(1, N+1):
        short = []
        tall = []
        for l_list in length_list:
            # l_list에 해당 숫자가 있다면, short, tall 에 맞게 숫자 추가하기
            if i in l_list:
                i_idx = l_list.index(i)
                # print(i, l_list, i_idx) => 5 [1, 5, 4, 2] 1
                for s in range(0, i_idx):
                    if s not in short:
                        short.append(s)
                for t in range(i_idx+1, len(l_list)):
                    if t not in tall:
                        tall.append(t)
            if len(short) + len(tall) == N-1:
                if i not in result:
                    result.append(i)
                    cnt += 1
    print('#{} {}'.format(t, cnt))
    # print(result)