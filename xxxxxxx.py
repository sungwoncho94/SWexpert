
# 고민해보기
'''
a = 0
def test():
    global a
    a += 1
    return a

print(test())
'''
# bit를 이용해 부분집합 구하기

cnt = 0
arr = [1, 2, 3, 4, 5, 6]   # n=6 이니까 2^6개만큼의 부분집합이 만들어질 수 있다.

n = len(arr)

for i in range(1<<n):  # 1<<n : 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교  /  n, n+1 결과값은 같지만 n+1일 때는 항상 0이라서 할 필요 없음
        if i & (1<<j):  # i의 j번째 비트가 1이면, j번째 원소 출력
            print(arr[j], end=" ")
    cnt += 1
    print()
print()
print(cnt)