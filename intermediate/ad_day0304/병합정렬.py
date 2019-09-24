T = int(input())

# 리스트를 나누는 함수 merge_sort
def merge_sort(n_list):

    # 반씩 자르는 list의 길이가 1이 되면 끝내고(return 하고) 다시 합치기 시작
    if len(n_list) == 1:
        return n_list

    # n_list를 left, right로 나눔
    mid = len(n_list)//2
    left = n_list[:mid]
    right = n_list[mid:]

    # left, right가 1이 될 때 까지 계속 나눔
    left_1 = merge_sort(left)
    right_1 = merge_sort(right)

    # 왼쪽부터 오른쪽 순서대로 병합하는 merge함수
    return merge(left_1, right_1)


# 왼쪽부터 오른쪽 순서대로 병합해주는 함수
def merge(left, right):

    # merge를 하는 순간에 left[-1]과 right[-1]을 비교한다
    global cnt
    if left[0] > right[0]:
        cnt += 1

    i = 0
    j = 0
    idx = 0
    result_list = [0] * (len(left) + len(right))  # 결과 리스트

    # left = i / right = j 로 왼쪽부터 훑어나가면서 i와 j 둘 중 하나가 끝에 도달할 때 까지
    while (i < len(left)) and (j < len(right)):
        
        # left, right를 비교하며 더 작은 값을 result에 더해준다
        if left[i] < right[j]:
            result_list[idx] = left[i]
            idx += 1
            i += 1
        else:
            result_list[idx] = right[j]
            idx += 1
            j += 1

    # 위 while이 끝날 때, 처음부터 left, right의 개수가 맞지 않거나, 
    # left, right중 한 쪽만 작은 숫자가 있어서 한 쪽만 정렬되고 끝날 수 있음.
    while i < len(left):
        result_list[idx] = left[i]
        idx += 1
        i += 1

    while j < len(right):
        result_list[idx] = right[j]
        idx += 1
        j += 1

    return result_list


for t in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(n_list)

    print("#{} {} {}".format(t, result[N//2], cnt))

    
