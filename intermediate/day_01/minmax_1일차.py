'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
출력
#1 630739
#2 740510
#3 838110
'''
T = int(input())

for t in range(1, T+1):
    N = int(input())  # 정수 n의 수
    num_list = list(map(int, input().split()))

    # max구하기
    max_num = 0
    for n in range(N):
        if num_list[n] >= max_num:
            max_num = num_list[n]
        else:
            max_num = max_num

    # min구하기
    min_num = num_list[0]
    for n in range(N):
        if num_list[n] <= min_num:
            min_num = num_list[n]
        else:
            min_num = min_num

    result = max_num - min_num
    print(f'#{t} {result}')

