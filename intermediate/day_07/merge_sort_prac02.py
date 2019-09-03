def merge_sort(m_list):
    if len(m_list) <= 1:
        return m_list
    
    # 1. 최소단위까지 나누기
    mid = len(m_list) // 2
    left = m_list[:mid]  # 처음부터 ~ 중간까지
    right = m_list[mid:]  # 처음부터 끝까지

    # 1.1 재귀호출하여 len(list)가 1이 될 때 까지 나눔
    left = merge_sort(left)
    right = merge_sort(right)

    # 2. 분할된 list 병합
    return merge(left, right)

def merge(left, right):
    result = []  # 최종 병합 result

    while len(left) > 0 and len(right) > 0:  # 양쪽 list에 원소가 있으면 계속 실행
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:  # 왼쪽 리스트에 원소가 남아있는 경우
        result.extend(left)
    if len(right) > 0:  # 오른쪽 리스트에 원소가 남아있는 경우
        result.extend(right)
    return result

data = [69, 10, 30, 2, 16, 8, 31, 22]
print(merge_sort(data))
