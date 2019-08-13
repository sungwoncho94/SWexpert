# 회문검사하는 함수를 만든다
# 전체 문자열판을 받아옴
# 가로방향으로 N-M해서 단어 뽑고, 회문검사
# 세로방향으로도 실시

T = int(input())

def pal(x):
    return True if x == x[::-1] else False

for t in range(1, T+1):
    matrix = []

    N, M = map(int, input().split())
    F = N - (M-1)

    result = ''
    
    for n in range(N):
        str_list = list(map(str, input()))
        matrix.append(str_list)

    for n in range(N):  # 0부터 N-1행까지 돌 것
        for f in range(F):  # N - M 열 까지만 순회
            test_str = ''
            for m in range(M):  # 글자 수 만큼 더하면서 단어 만든다
                test_str += matrix[n][f+m]
            if pal(test_str) == True:
                print(f'#{t} {test_str}')

    for n in range(N):  # 0부터 N-1행까지 돌 것
        for f in range(F):  # N - M 열 까지만 순회
            test_str = ''
            for m in range(M):
                test_str += matrix[f+m][n]

            if pal(test_str) == True:
                print(f'#{t} {test_str}')
