'''
[제약 사항]
N 과 M은 3 이상 20 이하이다.
[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 
그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
두 번째 줄에는 Ai,
세 번째 줄에는 Bj 가 주어진다.
[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
입력
10
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3
출력
#1 30
#2 63
'''

T = int(input())

for t in range(1, T+1):
    NM_len = list(map(int, input().split()))  # 3 <= N, M <= 20

    N_len = NM_len[0]  # N리스트 길이 
    M_len = NM_len[1]  # M리스트 길이

    N_list = list(map(int, input().split()))  # 실제 N리스트
    M_list = list(map(int, input().split()))  # 실제 M리스트

    # 긴단어배열, 짧은단어배열 정의
    if N_len > M_len:
        long_list = N_list
        short_list = M_list
    else:
        long_list = M_list
        short_list = N_list

    result = 0

    # 긴 단어배열의 0번부터 l-s번까지 시작 번호 바꾸기
    # 짧은단어는 항상 0부터 시작이다.
    for l in range(len(long_list) - len(short_list)+1):
        temp = 0  # l숫자가 바뀔때마다 temp = 0으로 초기화
        for s in range(len(short_list)):
            temp += short_list[s] * long_list[l+s]
        if temp > result:
            result = temp
        else:  # (temp < result)
            result = result
    print(f'#{t} {result}')

'''
짧은단어길이 = 3일 때
    for s in range(len(long_list) - len(short_list)+1):
        
        temp = short_list[0]*long_list[s] + short_list[1]*long_list[s+1] + short_list[2]*long_list[s+2]

        if temp > result:
            result = temp
        else:
            result = result
    print(result)
'''
