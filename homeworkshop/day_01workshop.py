# n = 5; m = 9

# print((('*' * n) + '\n') * m)

import math

a = int(input())
b = int(input())
c = int(input())

# x1 = ((-b)+ (b*b - 4*a*c)**0.5 )/2*a
# x2 = ((-b)+ (b*b + 4*a*c)**0.5 )/2*a



x1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
print(x1)
print(x2)