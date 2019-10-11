'''
트리-전위순회
부모 - Left값  ( 부모보다 작은 수 )
     - Right값 ( 부모보다 큰 수 )
'''

# class Tree: 라고만 해도 무방
class Node(object):
    def __init__(self, value):
        self.value = value  # 자신이 관리하는 값
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):  # 초기화 함수
        # 트리는 root노드가 필수임
        self.root = None

    def add(self, value):
        # root가 없으면 root에 현재 값을 넣는다
        # Node라는 클래스도 생성해줘야함
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value, self.root)  # 재귀적인 저장 함수

    def _add(self, value, node):
        # value는 저장하려는 숫자. root보다 작으면 왼쪽, 크면 오른쪽에 저장
            else:
        if node.value > value:
            if node.left == None:
                node.left = Node(value)
            else:
                # left에 node가 있으면, 그 아래에 저장
                self._add(value, node.left)
        else:
            if node.right == None:
                node.right = Node(value)
                self._add(value, node.right)

    def printAll(self):
        if self.root == None:
            return
        else:
            self._print(self.root)

    def _print(self, node):
        if node != None:
            print(node.value)  # 자기자신부터 출력 --> 전위법
            self._print(node.left)
            # print(node.value)  # 자신을 중간에 출력 --> 중위법
            self._print(node.right)
            # print(node.value)  # 자신을 마지막에 출력 --> 후위법

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node == None:
            level = -1
            return False
        level += 1
        if node.value == key:
            return True
        if node.value > key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

t = Tree()
s = [4, 8, 3, 1, 56, 35, 8, 82, 34]
for i in s:
    t.add(i)

level = 0

t.printAll()  # 전체 저장값 출력.  / 전위, 중위, 후위 설정

print(t.find(34))
