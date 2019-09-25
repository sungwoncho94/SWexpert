# num_list를 change번 만큼 섞는 함수를 만든다.
# random으로 change번을 섞은 후, max_num인지 살펴보기
def shuffle(num_list, change):
    for idx in range(len(num_list)-1):  # 0~N-2번 idx를 기준으로 잡고,
        for idx2 in range(idx, len(num_list)):  # idx ~ N-1번 idx를 바꿀건데,
            






T = int(input())

for t in range(1, T+1):
    temp_list = list(map(str, input().split()))
    str_num, change = temp_list[0], int(temp_list[1])
    
    # list에 숫자로 바꿔서 하나씩 넣을 것
    num_list = []
    for s in str_num:
        num_list.append(int(s))
'''
    # num_list가 두개일때는 횟수만큼 무조건 바꾸기
    if len(num_list) == 2:
        for c in range(change):
            num_list[0], num_list[1] = num_list[1], num_list[0]
        print(num_list)
    # 세개 이상일때는 횟수마다 idx 1이상에서 가장 큰 값 찾고, idx -1까지 가장 작은 값 찾아서 바꾼다
    else:  # if num_list = [3, 5, 4, 2, 1, 6]
        for c in range(change):
            # 매번 바꿀때마다 max, min값 초기화
            max_num = 0
            min_num = 0

            # 0 < idx 에서 가장 큰 값 찾기  [5, 4, 2, 1, 6]
            max_num = max(num_list[1:])  # max_num = 6
            # idx < N-1 에서 가장 작은 값 찾기  [3, 5, 4, 2, 1]
            min_num = min(num_list[:len(num_list)-1])  # min_num = 1

            num_list[num_list.index(max_num)], num_list[num_list.index(min_num)] = num_list[num_list.index(min_num)], num_list[num_list.index(max_num)] 
            
            print(num_list)
'''
