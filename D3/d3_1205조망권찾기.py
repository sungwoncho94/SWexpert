T = 10  # 총 문제 개수

for t in range(1, T+1):
    test_len = int(input())  # 문제마다 주어지는 test_case 길이
    building = list(map(int, input().split()))

    temp = 0  # 각 라인마다 확보되는 조망권 수
    result = 0  # temp를 더할 값 = 최종 답

    # 건물은 양옆 2칸을 제외하고 지어져 있음.
    for n in range(2, test_len-2):
        a = building[n] - building[n-2]
        b = building[n] - building[n-1]
        c = building[n] - building[n+1]
        d = building[n] - building[n+2]

        # 만약, a, b, c, d>= 일 때, min(a, b, c, d)의 값이 조망권 확보되는 집 개수임
        if a >= 0 and b >= 0 and c >= 0 and d >= 0:
            temp = min(a, b, c, d)
        else:
            temp = 0
        result += temp
    print(f'#{t} {result}')


''' 
min 함수 안쓰고 풀기
        # 만약, a, b, c, d>= 일 때, min(a, b, c, d)의 값이 조망권 확보되는 집 개수임
        # min함수 쓰지 말고 작성
        if a >= 0 and b >= 0 and c >= 0 and d >= 0:
            # a와 b비교
            if a >= b:
                temp = b
            # (a, b) & c비교
            if temp >= c:
                temp = c
            # (a, b, c) & d비교
            if temp >= d:
                temp = d
            if temp <= 0:
                temp = 0
        else: temp = 0
        result += temp
    print(f'#{t} {result}')
'''
