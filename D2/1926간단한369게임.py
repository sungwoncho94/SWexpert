N = int(input())

for num in range(1, N+1): # 15, 16, ..
    str_num = str(num)  # '15'  /  '16'
    result = ''  # 전체 숫자가 들어가야하니까, 숫자 for문 돌리기 전에 result 초기화
    for s in str_num:  # 1 5 / 1 6
        if '3' in s:
            s = s.replace('3', '-')
        if '6' in s:
            s = s.replace('6', '-')
        if '9' in s:
            s = s.replace('9', '-')
        result += s
    if '-' in result:
        result2 = ''
        for r in result:
            if r == '-':
                result2 += r
        print(result2, end=" ")
    else:
        print(result, end=" ")