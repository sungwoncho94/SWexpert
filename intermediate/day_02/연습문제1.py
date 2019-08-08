'''
5*5 2차 배열에 무작위로 25개의 숫자로 초기화한 후, 
25개의 각 요소에 대해서 그 요소와 이수한 요소와의 차의 절대값을 구하라.
ex.
n 2 n
6 7 8
n 12 n
-> 12
25개 요소에 대해서 모두 조사하여 총합을 구하라.
'''
'''
import random

N = list(range(1, 26))
matrix = []

# 랜덤 1~25 매트릭스 작성
# for i in range(5):
#     list_i = []
#     for j in range(5):
#         rdm = random.choice(N)
#         N.remove(rdm)
#         list_i.append(rdm)
#     matrix.append(list_i)


# 선생님답
arr = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

sum_num = 0

# 벽인지 아닌지 구분하는 함수
def isWall(x, y):
    if x < 0 or x >= 5 :
        return True
    if y < 0 or y >= 5:
        return False

def my_abs(x, y):
    if int(x) > int(y):
        result = int(x) - int(y)
    else:
        result = int(y) - int(x)
    return result

for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum_num += my_abs(arr[x][y], arr[testX][testY])

print(sum_num)
'''
# 테스트용 배열
arr = [
    [1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 1], 
    [1, 0, 0, 0, 1], 
    [1, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1],
    ]

def my_abs(a, b):
    if a >= b:
        result = a - b
    else:
        result = b - a
    return result

def isWall(x):
    if x < 0 or x >= 5:
        return True
    else:
        return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sum_num = 0

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):  # 사방탐색
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX) + isWall(testY) == False:
                sum_num += my_abs(arr[x][y], arr[testX][testY])

print(sum_num)





