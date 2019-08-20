T = int(input())

for t in range(1, T+1):
    string = input()
    check_list = []
    flag = 1

    # check_list에 (, {를 순서대로 넣는다.
    for i in string:
        if i == '(' or i == '{':
            check_list.append(i)

        elif i == ')':
            if len(check_list) == 0:
                flag = 0
                break
            else:
                if check_list[-1] == '(':
                    check_list.pop()
                else:
                    flag = 0
                    break

        elif i == '}':
            if len(check_list) == 0:
                flag = 0
                break
            else:
                if check_list[-1] == '{':
                    check_list.pop()
                else:
                    flag = 0
                    break

    if flag == 1 and len(check_list) == 0:
        print('#{} 1'.format(t))
    elif flag == 0:
        print('#{} 0'.format(t))
    else:
        print('#{} 0'.format(t))