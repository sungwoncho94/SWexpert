
'''
3
0 1 1 0 0 1 0 0 0 0
60
1 1 1 1 1 1 1 1 1 1
128
0 1 0 1 0 1 0 1 0 1
128

#1 5
#2 4
#3 -1

0 0 0 0 0 0 0 0 0 1
793881

#1 10
'''

T = int(input())

for t in range(1, T+1):
    temp_list = list(map(int, input().split()))
    num_list = []
    target = int(input())
    div_target = []
    flag1 = 1
    result = 99999
    
    # 누를 수 있는 숫자 뽑기
    for p in range(10):
        if temp_list[p] == 1:
            num_list.append(p)
    # print(num_list) = [1, 2, 5]

    str_target = str(target)
    for tar in str_target:
        div_target.append(int(tar))
    # print(div_target) = [6, 0]

    for div in div_target:
        # target을 나눈 숫자가 num_list안에 없으면 flag1을 0으로 만든다.
        if div not in num_list:
            flag1 = 0
            break
    
    # 숫자조합만으로 target을 만들 수 있다면 그대로 출력하고 끝
    if flag1 == 1:
        print('숫자조합으로 가능!')
        print('#{} {}'.format(t, len(div_target)+1))

    # 숫자조합만으로 target을 만들 수 없다면
    else:
        # flag2는 False인 상태
        flag2 = 0

        # 1로는 나누지 않는다.  //  target//2 까지만 i를 돌려도 된다.
        for i in range(2, target//2):
            # 새로운 숫자로 나눌때마다 새로운 div_target_2 생성  //  div_target_2 = 나눠진 target을 분해해놓은것
            div_target_2 = []

            target = target // i  # (target = 30)
            str_target = str(target)
            for tar in str_target:
                div_target_2.append(int(tar))  # [3, 0]

            for div in div_target_2:  # div = 3, 0
                # target을 나눈 숫자가 num_list안에 없으면 flag1을 0으로 만든다.
                if div not in num_list:
                    # 최상위for문으로 되돌아간 후 다시 다음 i로 나누기위해선 target을 원상태로 복원시켜줌
                    flag2 = 0
                    target = target * i
                    break
                # div가 num_list안에 있다면 flag2 -> 1로 바꾼다. 
                # 모든 div가 num_list안에 있으면 flag는 1인 상태 / 하나라도 없으면 0이 될 것. (break를 했으니까)
                elif div in num_list:
                    flag2 = 1

            # for문이 끝난 후, i 일때 모든 div가 num_list안에 있으면
            if flag2 == 1: 
                temp_result = len(str(i)) + len(div_target_2) + 2
                if temp_result < result:
                    result = temp_result
                    print_i = i
                    print_target = div_target_2


        # 모든 i를 다 돈 후, result가 존재한다면
        if result < 9999:  # 원래 result는 99999였음
            print('#{} {}'.format(t, result))
            print(print_i, print_target)
        else:
            print('#{} -1'.format(t))

