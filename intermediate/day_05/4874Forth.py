T = int(input())

for t in range(1, T+1):
    stack = []
    cal_list = input().split()
    cal_list.pop()
    temp = 0
    flag = 1
    # 10 2 + 3 4 + *

    for c in cal_list:

        # 계산 한번 끝냄
        if c.isdigit() == True:
            stack.append(int(c))

        elif c == '+' or c == '-' or c == '*' or c == '/':
            try:
                if c == '+':
                    temp = stack[-2] + stack[-1]  
                elif c == '-':
                    temp = stack[-2] - stack[-1]
                elif c == '/':
                    temp = stack[-2] / stack[-1] 
                elif c == '*':
                    temp = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)

            except:
                print('#{} error'.format(t))
                flag = 0
                break

    result = stack.pop()
    if flag == 1:
        print('#{} {}'.format(t, result))

'''
elif c == '.':
            if len(stack) == 0:
                print('#{} {}'.format(t, result))
            else:
                print('#{} error'.format)
                '''