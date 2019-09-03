# 첫 번째 노드로 삽입하는 알고리즘
def addtoFirst(data):  # 첫 노드에 데이터 삽입
    global Head

    Head = Node(data, Head)  # 새로운 노드 생성

def add(pre, data):  # pre 다음에 data삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None  # 마지막 노드를 찾을 때까지
            p = p.link
        p.link = Node(data, None)
    
def delete(pre):  # pre 다음 노드 삭제
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link