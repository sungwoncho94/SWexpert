# T = int(input())

# for t in range(1, T+1):
#     # N = 수열의 길이 / M = 추가 횟수 / L = 출력할 idx번호
#     N, M, L = map(int, input().split())
#     n_list = list(map(int, input().split()))
    
#     for m in range(M):
#         idx, num = map(int, input().split())
#         n_list.insert(idx, num)

#     print('#{} {}'.format(t, n_list[L]))

T = int(input())

for t in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    n_list = list(map(int, input().split()))

    for m in range(M):
        idx, num = map(int, input().split())
        left_list = n_list[:idx]
        right_list = n_list[idx:]

        new_list = left_list + [num] + right_list

        n_list = new_list

    print('#{} {}'.format(t, n_list[L]))