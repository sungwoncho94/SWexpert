'''
3
123 1
2737 1
32888 2

10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645

#1 321
#2 7732
#3 88832
'''
import copy

def make_num(num_list):
    global num_num

    str_num = ''
    for i in num_list:
        str_num += str(i)
    num_num = int(str_num)

    return num_num

T = int(input())

for t in range(1, T+1):
    temp_list = list(map(str, input().split()))
    str_num, change = temp_list[0], int(temp_list[1])
    
    # list에 숫자로 바꿔서 하나씩 넣을 것
    num_list = []
    for s in str_num:
        num_list.append(int(s))
    # print(num_list)  =  [1, 2, 3]

    copy_list = copy.deepcopy(num_list)

    cnt = 0
    max_num = 0

    # shuffle 돌릴 떄마다 tc_list에 넣어놓고, 여기서 꺼내서 또 돌리고 또 넣고 반복.....?
    temp_change_list = []
    if len(num_list) == 2:
        for c in range(change):
            num_list[0], num_list[1] = num_list[1], num_list[0]
        print('#{} {}'.format(t, make_num(num_list)))
    else:
        for idx in range(len(num_list)-1):  # 0~N-2번 idx를 기준으로 잡고,
            for idx2 in range(idx+1, len(num_list)):  # idx ~ N-1번 idx를 바꿀건데,

                # copy리스트 만들어놓은다음 다시 초기화
                copy_list[idx], copy_list[idx2] = num_list[idx2], num_list[idx]
                
                # 처음 돌리는거니까 모두 append
                temp_change_list.append(copy_list)
                copy_list = copy.deepcopy(num_list)

        # for문 두바퀴 다 돌았을 때 cnt += 1
        cnt += 1
        # print('temp_change_list=', temp_change_list)

        while cnt < change:
            for a in range(len(temp_change_list)):

                # temp_change_list에서 하나씩 빼서 for문 두번씩 다 돌려
                num_list = temp_change_list.pop(0)
                for idx in range(len(num_list)-1):  # 0~N-2번 idx를 기준으로 잡고,
                    for idx2 in range(idx+1, len(num_list)):  # idx ~ N-1번 idx를 바꿀건데,

                        # 바꾸려는 목표인 num_list를 copy해야한다
                        copy_list = copy.deepcopy(num_list)

                        # copy리스트 만들어놓은다음 다시 초기화
                        copy_list[idx], copy_list[idx2] = num_list[idx2], num_list[idx]

                        # temp_change_list에 없으면 append
                        if copy_list not in temp_change_list:
                            temp_change_list.append(copy_list)
                        copy_list = copy.deepcopy(num_list)

            # print('cnt=', cnt, 'list', temp_change_list)
            cnt += 1

        # while문이 다 끝나고 나면 max 값 뽑는다.
        for tc in temp_change_list:
            if max_num < make_num(tc):
                max_num = make_num(tc)

        print('#{} {}'.format(t, max_num))

