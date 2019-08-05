# workshop
'''
class Circle:
    pi = 3.14
    x = y = r = 0

# __init__ : 생성될 때, self.변수 = 변수 로 지정해준다
# self, r, x, y는 인스턴스가 생성될 때 필수로 필요한 변수들 -> 생성될 때 값을 지정해줘야함.
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

test_circle = Circle(3, 2, 4)

print(f'넓이 : {test_circle.area()}')
print(f'둘레 : {test_circle.circumference()}')
'''

# homework

'''
test_list = [1, 2, 3]

test_list.append({'a':4, 'b':5})
print(test_list)

test_list.extend([6, 7])
print(test_list)

c = test_list.pop()
print(test_list)
'''



