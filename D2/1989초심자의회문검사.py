T = int(input())

for t in range(1, T+1):
    stc = input()
    stc2 = stc.strip()

    stc_list = []
    for s in stc2:
        stc_list.append(s)

    re_stc = []

    for i in range(len(stc_list)-1, -1, -1):
        re_stc.append(stc_list[i])

    if re_stc == stc_list:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')