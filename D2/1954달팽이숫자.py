T = int(input())
​
for t in range(1, T+1):
    N = int(input())
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
	
	# 빈 N*N리스트
    matrix = [[0 for i in range(N)] for j in range(N)]
	'''
	nlist = [0] * N
    matrix = [nlist] * N
	이렇게 만들면 동일한 nlist가 N번 반복되서 matrix의 열마다 같은 숫자가 나온다
	'''
   
    # change_list 정하기 --> 이 리스트 내의 값이 나오면 방향 바꾸기
    change_list = []
    
    a = n = temp = minus = 0
    while a < N * N:
        n += 1
        a = n * N - minus
        if n % 2 == 1:
            temp += 1
        minus = minus + temp
        change_list.append(a-1)
        # change_list = [5, 9, 13, 16, 19, 21, 23, 24, 25]
​
    i = n = 0
    x = y = 0
    while n < N * N:
        n += 1
        matrix[x][y] = n
        x += dx[i]
        y += dy[i]
        if n in change_list:
            i += 1
            if i == 4:
                i = 0
    
    print(f'#{t}')
    for n in range(N):
        result = matrix[n]
        if n != 0:
	        print()
        for r in result:
            print(r, end=' ')
    print()
    
    