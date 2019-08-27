# list.remove(' ') 는 list의 왼쪽부터 ' '안의 str을 지우는 함수. 무조건 왼쪽부터 지운다
# del 사용법 = del list[ ]
T = int(input())

for t in range(1, T+1):
    str_list = list(map(str, input()))
    index = len(str_list)
    flag = flag2 = 1

    while flag == 1:
        if flag2 == 0:
            break
        #i = 1  # 항상 처음부터 다시 시작
        for i in range(1, index):  # 처음부터 훑어가면서,
            # 같은 글자가 있다면 글자 두개를 삭제하고 for문으로 돌아가라
            if str_list[i-1] == str_list[i]:
                del str_list[i-1]
                del str_list[i-1]
                index = len(str_list)

                # 두 글자를 지웠을 때 str_list가 하나밖에 없다면 flag=0으로 바꾸고 끝
                if index == 1:
                    flag = 0
                break
            # else:
            #     print('통과{}'.format(str_list))
        #print(str_list)
        # str_list에서 하나라도 같은게 나오면 flag=1이고, while문으로 돌아가게함.
        # 같은게 나오지 않으면 flag는 여전히 0이고, 끝낸다.
        flag2 = 0
        for a in range(1, index):
            if str_list[a-1] == str_list[a]:
                flag2 = 1
                break

    print('#{} {}'.format(t, len(str_list)))