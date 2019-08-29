for t in range(1, 11):
    N = int(input())
    cal_list = input()

    stack = []
    result = ''

    # stack 안에서의 우선순위
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, ')': 0}
    # stack 밖에서의 우선순위
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2, ')': 0}

    for c in cal_list:
        # print(c, result, stack)
        # c가 숫자라면
        if c.isdigit() == True:
            result += c
        # c가 숫자가 아니라면
        else:
            # stack에 아무것도 없다면 일단 기호 넣기
            if len(stack) == 0:
                stack.append(c)
            
            elif stack:
                if c == ')':
                    while stack[-1] != '(':
                        a = stack.pop()
                        result += a
                    stack.pop()

                elif icp[c] > isp[stack[-1]]:
                    stack.append(c)
                
                else:  # elif icp[c] <= isp[stack[-1]]:
                    while isp[stack[-1]] >= icp[c]:
                        a = stack.pop()
                        if not stack:
                            result += c
                            break
                        result += a
                    stack.append(c)
    if len(stack) == 1:
        a = stack.pop()
        result += a
    
    # print(result)

    stack = []
    for r in result:
        if not stack:
            stack.append(int(r))
        elif stack:
            if r.isdigit():
                r = int(r)
                stack.append(r)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if r == '+':
                    temp = b + a
                elif r == '-':
                    temp = b - a
                elif r == '/':
                    temp = b / a
                elif r == '*':
                    temp = b * a
                stack.append(temp)
                # print(stack)
    final = stack.pop()
    print('#{} {}'.format(t, final))
        
