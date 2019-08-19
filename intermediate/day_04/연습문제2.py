stack = [0] * 100
top = -1
str = '()()((()))'
# str2 = '((()((((()()((()())((())))))'

flag = True

for i in range(len(str)):
    if str[i] == '(':
        top += 1
        stack[top] = str[i]
    elif str[i] == ')':
        if top == 1-:
            flag = False
            break
        top -= 1

    if top == -1 and flag:
        print('correct')
    else:
        print('wrong')