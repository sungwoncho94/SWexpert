# import sys
# from pprint import pprint
#
# sys.stdin = open("5643.txt")

T = int(input()) # 전체 테스트케이스 개수

def printmat(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

for tc in range(1,T+1):
    N = int(input()) #첫 번째 TC의 N 학생수
    M = int(input()) #첫 번째 TC의 M 키 비교 횟수
    Answer=0
    Data = []
    for i in range(N+1):
        Data.append( [999]*(N+1) )
    for i in range(N+1):
        for j in range(N+1):
            if i==j : Data[i][j]=0
    # pprint(Data)
    for i in range(M):
        x,y = map(int,input().split())
        Data[x][y] = 1
    # pprint(Data)
    for k in range(1,N+1): #거쳐가는 노드
        for i in range(1,N+1): #출발하는 노드
            for j in range(1,N+1): #도착하는 노드
                if Data[i][j] > Data[i][k]+Data[k][j]:
                    Data[i][j] = Data[i][k] + Data[k][j]
    # printmat(Data)

    for i in range(1,N+1):
        flag = True
        for j in range(1,N+1):
            if Data[i][j] >= 999 and Data[j][i] >= 999:
                flag = False
                break
        Answer += ( 1 if flag else 0 )
    print("#{} {}".format(tc,Answer))