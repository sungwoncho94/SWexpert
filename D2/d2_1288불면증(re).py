'''
예를 들어 N = 1295이라고 하자.
첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.
두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9이다.
현재까지 본 숫자는 0, 1, 2, 5, 9이다.
세 번째로 3N = 3885번 양을 센다. 현재 본 숫자는 3, 5, 8이다.
현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.
네 번째로 4N = 5180번 양을 센다. 현재 본 숫자는 0, 1, 5, 8이다.
현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.
다섯 번째로 5N = 6475번 양을 센다. 현재 본 숫자는 4, 5, 6, 7이다.
현재까지 본 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9이다.
5N번 양을 세면 0에서 9까지 모든 숫자를 보게 되므로 민석이는 양 세기를 멈춘다.
'''
''' input
5
1
2
11
1295
1692
'''

# test_case = int(input())   # 총 몇 건의 테스트케이스가 있는지


# # 첫번째 테스트케이스 가정 (N)
num = int(input())    # int(input())  첫번째 테스트 케이스
result = []           # 결과 리스트
k = 1                 # 횟수

while len(result) < 10:                # input된 num은 바꾸면 안되니까 temp란 변수에 담아서 변환
    temp = num * k                     # 왜 temp = num*k를 여기서 할까???
    for i in range(len(str(temp))):    # for문 3번 반복 (0,1,2)
        a = temp % 10
        temp = int(temp/10)
        if a not in result:
            result.append(a)
            print(result)
    k += 1                              # k =+ 1 을 하면 for문이 끝나고 while로 들어가는건가?

print(num*(k-1))

''' 희철님 코드
N = int(input())
num_list = []
set_list = []
k = 0

while len(set_list) < 10:
   k += 1
   number = k * N
   str_number = str(number)
   for i in range(len(str_number)):
       num_list.append(str_number[i])
       set_list = set(num_list)
print(k)
print(set_list)
'''
