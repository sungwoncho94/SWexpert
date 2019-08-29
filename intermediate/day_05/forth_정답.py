T = int(input())

for t in range(1, T+1):
    stack = []
    data = list(input().split())
    data.pop()
    result = 0
    n = len(data)
    satck = []
    flag = 1

    for i in range(n-1):  # 연산식 만큼 반복
        # 숫자이면 스택에 저장
        try:
            if data[i].isdigit():
                stack.append(data[i])
            else:  # 숫자가 아니면
            # 후위표기법 계산
            # 마지막 전 숫자 _ 연산자 _ 마지막 숫자
                num2, num1 = int(stack.pop()), int(stack.pop())
                if data[i] == "+":
                    result = num1 + num2
                if data[i] == "-":
                    result = num1 - num2
                if data[i] == "*":
                    result = num1 * num2
                if data[i] == "/":
                    result = num1 // num2
                stack.append(result)
        except:
            flag = 0
            

    # stack의 길이가 1인 경우만 정답
    if len(stack) == 1 and flag == 1:
        print('#{} {}'.format(t, result))
    elif flag == 0 or len(stack) > 1 or len(stack) == 0:
        print('#{} error'.format(t))