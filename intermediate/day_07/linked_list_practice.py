# 노드 클래스 정의
class Node:
    # Node가 정의될 때, 정의되는 Node의 value = 입력받은 value, Node의 next = next로 초기화함
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list 클래스 정의
class linkedlist:
    # head, tail, before, current, num_of_data를 갖는다
    def __init__(self):
        
        dummy = Node('head')
        self.head = dummy
        self.tail = dummy

        self.before = None
        self.current = None

        self.num_of_data = 0


    # 가장 뒤에 Node 추가하는 append 구현
    def append(self, data):
        new_node = Node(data)
        
        self.tail.next = new_node  # tail이 new_node를 가르키게 한다
        self.tail = new_node  # 가장 끝 데이터 = new_node

        self.num_of_data += 1

    
    # 현재 데이터를 삭제하는 delete 구현
    def delete(self):
        del_data = self.current.data

        # 마지막 데이터라면 이전 데이터를 마지막 데이터로 바꾼다
        if self.current is self.tail:
            self.tail = self.before

        # 이전 노드가 내 다음 노드를 가르키도록
        self.before.next = self.current.next
        # 이전 노드를 현재 노드로 바꾼다
        self.current = self.before

        self.num_of_data -= 1

        return del_data


    # 맨 앞의 노드를 검색하는 first 함수
    def first(self):
        if self.num_of_data == 0:
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    # 현재의 다음 노드를 검색해주는 next 함수
    def next(self):
        if self.current.next == None:
            return None
        
        self.before = self.current
        self.current = self.current.next

        return self.current.data


    # linked list 개수 알려주는 size 함수
    def size(self):
        return self.num_of_data


# Linked List 실행해보기

# linkedlist클래스의 인스턴스 l_list 만들기
l_list = linkedlist()
#[5, 2, 1, 2, 7, 2, 11]
l_list.append(1)
l_list.append(2)
l_list.append(3)
l_list.append(4)
l_list.append(5)
l_list.append(6)
l_list.append(7)

print('first : ', l_list.first())
print('next : ', l_list.next())
print('current : ', l_list.current.data)
print('delete 시행')
l_list.delete()
print('current : ', l_list.current.data)
print('tail : ', l_list.tail.data)
print(l_list.head.data)
