# x = int(input())   # x = 8   l = 2, u = 3


# for n in range(1, x+1):
#     while n ** 2 <= x:
#         n += 1
#         lower_num = n - 1
#         upper_num = n
# print(lower_num, upper_num)

# while upper_num - lower_num >= 0.001:
#     new_num = (upper_num + lower_num) / 2

#     if new_num ** 2 > x:
#         upper_num = new_num
#     else:
#         lower_num = new_num
# print(f'{lower_num} <= {x}제곱근 <= {upper_num}')
    

# ----------------------------

import math

def my_sqrt(n):
    x, y = 1, n
    result = 1		# 우리가 추측하는 제곱근 result
    
    while abs(result ** 2 - n) > 0.0000001:
        result = (x + y) / 2
        if result ** 2 < n:
            x = result
        else:
            y = result
    return result

print('math.sqrt : \t', math.sqrt(2))
print('my_sqrt : \t', my_sqrt(2))