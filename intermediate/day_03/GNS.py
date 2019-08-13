T = int(input())
for t in range(1, T+1):
    str_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count_list = [0] * 10
    t, N = list(input().split())
    num_list = list(map(str, input().split()))

    for n in range(int(N)):
        for i in range(10):
            if num_list[n] == str_list[i]:
                count_list[i] += 1
    
    print(t)
    for i in range(10):  # 0~9까지 count_list의 index 살펴보면서
        while count_list[i] > 0:
            if count_list[i] != 0:
                print(str_list[i], end=' ')
                count_list[i] -= 1
            elif count_list[i] == 0:
                i += 1

''' 선생님 답변
for t in range(1, T+1):
    temp = input()
    nums = input().split()

    cnt = [0] * 10

    for num in nums:
        cnt[getidx(num)] += 1

    ans = ''
    for i in range(10):
        ans += p[i] * cnt[i]
    print('#%d '%tc, ans)
'''