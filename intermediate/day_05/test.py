T = 10
for tc in range(1, T+1):
    N = int(input()) 
    icp = {'*':2,'/':2,'+':1,'-':1,'(':3}
    isp = {'*':2,'/':2,'+':1,'-':1,'(':0}
    token=[]
    que=[]
    string = input()

    for s in string:
        if s.isdigit():
            que.append(s)
        else: 
            if not token:
                token.append(s)
            elif token:
                if s == ')':
                    while token[-1] != '(':
                        a = token.pop()
                        que.append(a)
                    token.pop() 
                elif isp[token[-1]] < icp[s]:
                    token.append(s)
                else: 
                    while icp[s] <= isp[token[-1]]:
                        a = token.pop()
                        if not token:
                            que.append(a)
                            break
                        que.append(a)
                    token.append(s)
    print(que)