tc = int(input())
for tcc in range(1, tc+1):
    bi = str(input())
    te = str(input())
    b = len(bi)
    t = len(te)
    # 1011 1000 1110 0010
    bi_list = []
    te_list = []
    for i in range(b):
       if bi[i] == '1':
           new = '0'
       elif bi[i] == '0':
           new = '1'
       num = '{}{}{}'.format(bi[:i], new, bi[i + 1:b])
       ob = '{}{}'.format('0b',num)
       bi_list.append(int(ob, 2))
    print(bi_list)

    for i in range(t):
        for j in range(2):
            if te[i] == '0':
                neww = [1,2]
            elif te[i] == '1':
                neww = [2,0]
            elif te[i] == '2':
                neww = [0,1]
            numm = '{}{}{}'.format(te[:i], neww[j], te[i + 1:t])
            print(numm)
            cnt = 0
            for k in range(len(str(numm))):
                cnt += int(numm[k]) * (3 ** k)
            te_list.append(cnt)
    print(te_list)
    for x in range(len(bi_list)):
        for y in range(len(te_list)):
            if bi_list[x] == te_list[y]:
                ans = bi_list[x]

    print('#{} {}'.format(tcc,ans))