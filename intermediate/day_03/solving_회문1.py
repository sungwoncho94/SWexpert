T = 10

def pal(x):
    return True if x == x[::-1] else False

for t in range(1, T+1):
    matrix = []
    P = int(input())  # 찾을 회문 길이
    F = 8 - (P-1)  # 회문 검색할 시작index
    
    # input matrix 만들기
    for i in range(8):
        sentence = list(map(str, input()))
        matrix.append(sentence)
    
    cnt = 0  # 회문 개수

    for r in range(8):  # 0~7행 탐색
        for f in range(F):  # 0~마지막탐색index까지
            test = ''  # index가 바뀔때마다 단어 리셋
            for p in range(P):  # 회문 글자수만큼 탐색
                test += matrix[r][f+p]
            if pal(test):
                cnt += 1
    
    for r in range(8):  # 0~7행 탐색
        for f in range(F):  # 0~마지막탐색index까지
            test = ''  # index가 바뀔때마다 단어 리셋
            for p in range(P):  # 회문 글자수만큼 탐색
                test += matrix[f+p][r]
            if pal(test):
                cnt += 1

    print('#%d %d' % (t, cnt))
    