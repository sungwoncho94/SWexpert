T = int(input())

for t in range(1, T+1):
    stack = []
    cal_list = input().split()
    temp = 0
    flag = 1
    result = ''

    for c in cal_list:
        # print(c, stack)

        # 숫자가 들어오면 stack.append
        if c.isdigit() == True:
            stack.append(int(c))

        # 연산기호일 때
        elif c == '+' or c == '-' or c == '*' or c == '/':
            # stack의 길이가 2 이상일때만 pop() 두번
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop() 

                if c == '+':
                    temp = b + a
                    stack.append(temp)
                elif c == '-':
                    temp = b - a
                    stack.append(temp)
                elif c == '*':
                    temp = b * a
                    stack.append(temp)
                elif c == '/':
                    temp = b / a
                    stack.append(temp)
                # 연산자 아무것도 안나오고 숫자 . 나올 경우
                else:
                    result = 'error'
                    break
            else:
                result = 'error'
                break

        elif c == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
                break
            
            # stack의 길이가 1 이하 -> error    
        else:
            result = 'error'
            break

    print('#{} {}'.format(t, result))

'''
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
'''