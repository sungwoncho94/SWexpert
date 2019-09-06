def is_danjo(nums):
    for i in range(len(str(nums)) - 1):
        if int(str(nums)[i]) > int(str(nums)[i + 1]):
            return False
    return True

TC = int(input())

for t in range(1, TC + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_danjo = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            multiple_nums = nums[i] * nums[j]
            if is_danjo(multiple_nums) == True and multiple_nums > max_danjo:
                max_danjo = multiple_nums

    if not max_danjo:
        result = -1
    else:
        result = max_danjo
    print('#{} {}'.format(t, result))