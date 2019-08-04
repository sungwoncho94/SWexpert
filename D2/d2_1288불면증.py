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

T = int(input())

for t in range(1, T+1):
    num = int(input())
    sum_num = num
    num_list = []
    i = 0

    while len(num_list) < 10:
        str_num = str(num)
        for n in str(num):
            if n not in num_list:
                num_list.append(n)
        num += sum_num
        i += 1
    
    print(f'#{t} {str_num}')

    
    





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
