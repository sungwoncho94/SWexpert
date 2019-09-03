# 숫자 -> stack에 넣기
# 연산기호 icp, isp 정하기
T = int(input())

isp = {'(':0, '+':1, '-':1, '*':2, '/':2, ')':0}
icp = {'(':3, '+':1, '-':1, '*':2, '/':2, ')':0}

for t in range(1, T+1):
    str_list = list(map(str, input().split()))
    stack = []
    operator = []

    for s in str_list:
        if s.isdigit():
            stack.append(int(s))
            print(stack)
        else:
            if s == '(':
                operator.append(s)
                print(operator)
            else:
                if icp[s] > isp[operator[-1]]:
                    operator.append(s)
                else:
                    while icp[s] <= isp[operator[-1]]:
                        token = operator.pop()
                        stack.append(token)
    
    print(stack)