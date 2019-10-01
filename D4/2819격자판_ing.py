'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1

#1 23
'''

T = int(input())

for t in range(1, T+1):
    matrix = []
    result_list = []  # 만들어진 7자리 숫자를 넣을 list

    # matrix 완성
    for m in range(4):
        m_list = list(map(int, input().split()))
        matrix.append(m_list)
    
    for i in range(4):
        for j in range(4):
            