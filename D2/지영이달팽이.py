def iswall(arr,i,j): #i, j는 인덱스로 들어가야 함
    if i < 0 or i >= N:
        return True
    if j < 0 or j >= N :
        return True
    if arr[i][j] != 0:
        return True
    return False

if __name__ == "__main__":
    N = 3
    l = [i+1 for i in range(N*N)]
    # print(l)
    arr = [[0]*N for _ in range(N)]

    #꺾는 순간의 규칙 #처음가는 순간부터
    row = 0; col = 0; #시작점 잡기
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]
    idx = 0 #모듈러 연산으로 막아줘야
    k=0
    #값을 대입하기
    # for i in range(N):
    #     for j in range(N):
    #         row += d_row[idx]
    #         col += d_col[idx]

    num = 1
    while num < N*N:
        arr[row][col] = num
        print(arr)

        row += d_row[idx]
        col += d_col[idx]

        if iswall(arr,row,col):
            print(row, col)
            row -= d_row[idx]
            col -= d_col[idx]
            idx = (idx+1)%4
            row += d_row[idx]
            col += d_col[idx]
            print(row, col)
        num += 1