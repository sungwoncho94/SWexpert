class Poketmon:

    def __init__(self, name):  # 인스턴스가 생성될 때 name변수를 넘겨받아야함
        self.name = name
        self.level = 5
        self.hp = self.level * 20
        self.exp = 0

    def infor(self):  # 객체의 현재 상태를 알려주는 함수
        return self.name, self.level, self.hp, self.exp

    def bark(self, target):
        target.level -= 1
        print(f'{self.name}(이)가 울부지저따! {target.name}(은)는 기가 죽었다!')
        print(f'{target.hp + 20} -> {target.hp}')

    def normal_attack(self, target):
        damage = self.level * 5
        target.hp -= damage
        print(f'평범한 공격! {target.name}(은)는 {damage}만큼의 피해를 입었다.')
        print(f'{target.name}의 hp : {target.hp}')
        self.check_battle(target)  # 매 공격이 끝날때마다 배틀 상황 함수 호출

    def special_attack(self, target):
        damage = self.level * 8
        target.hp -= damage
        print(f'엄청난 공격! {target.name}(은)는 {damage}만큼의 피해를 입었다.')
        print(f'{target.name}의 hp : {target.hp}')
        self.check_battle(target)


    # 타겟이 죽었을 때, 내 스탯 알려주는 함수
    def check_battle(self):
        if target.hp <= 0:
            print(f'{target.name}(이)가 쓰러졌다!')
            self.exp += target.level * 15

            if self.exp >= self.level * 50:
                self.exp -= self.level * 50
                self.level += 1
                self.hp = self.level * 20
                print(f'Level Up!! {self.name}의 레벨이 {self.level}이 되었다! 현재 경험치는 {self.exp}/{self.level*50}이다.')

    # 배틀 시 매 턴마다 상황을 알려주는 함수
    # 공격자와 방어자, 스킬을 랜덤으로 정하는 battle함수 정의
    # 둘이 살아있을때 계속 반복
    def battle(self, target):
        count = 0

        while self.hp >= 0 and target.hp >= 0:
            print(f'###라운드 {count} ###')
            print(f'{self.name}의 hp : {self.hp}')
            print(f'{target.name}의 hp : {target.hp}')
            print('---------------------------------')

            attacker