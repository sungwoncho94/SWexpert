def partition(l, L, R):
    piv = l[L] # 얘를 임의대로 앞 수를 넣지 말고 L을 넣어야 하는 이유?
    i=L; j=R # L = 1; R=len(l)-1로 설명해야
    while i < j:
        while l[i] <= piv and i < N-1: # piv보다 작은게 나오면 갠춘, 큰게 나오면 제어해야
            i+=1
        while l[j] > piv and j > 0:
            j -=1
        # while문을 빠져나왔다면, 더 큰애가 left, 더 작은애가 right에 있어서 swap할 케이스란 뜻
        if i < j :
            temp =l[i]
            l[i] = l[j]
            l[j] = temp
    # 다 끝난 후에는 piv가 두 집단을 나누는 기준으로 위치해야(j번째 들어가면 됐음)
    temp = l[L]
    l[L] = l[j]
    l[j] = temp
    return j

def quick(l,L,R):
    if L < R:
        piv_idx = partition(l, L, R)
        quick(l, L, piv_idx-1)
        quick(l, piv_idx+1, R)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    q_list = list(map(int, input().split()))
    quick(q_list, 0, N-1)
    print('#%d %d' % (t,q_list[N//2]))