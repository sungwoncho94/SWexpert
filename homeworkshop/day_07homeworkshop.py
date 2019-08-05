# workshop
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        super().walk()

    def run(self):
        print(f'{self.name}! 달린다!')

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        super().eat()

    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('바둑이')

dog.walk()
dog.run()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
'''


# homework

class Calculator:
    count = 0

    def info(self):
        print('나는 계산기 입니다.')

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        print(f'{a} + {b}는 {a + b}입니다.')

    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')

cal = Calculator()

cal.info()

cal.add(1, 2)

cal.history()

