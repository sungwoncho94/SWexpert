def quick_sort(q_list):
    # list의 길이가 1보다 작다면, list를 반환하고 끝낸다.
    if len(q_list) <= 1:
        return q_list
    else:
        # list의 중간값을 pivot으로 설정
        pivot = q_list[len(q_list)//2]

        left, right, equal = [], [], []

        for q in q_list:
            if q > pivot:
                right.append(q)
            elif q < pivot:
                left.append(q)
            else:
                equal.append(q)
        
        return quick_sort(left) + equal + quick_sort(right)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    q_list = list(map(int, input().split()))
    result = quick_sort(q_list)
    
    print('#{} {}'.format(t, result[len(q_list)//2]))


