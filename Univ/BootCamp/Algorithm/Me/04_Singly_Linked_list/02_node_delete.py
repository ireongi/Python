## 클래스와 함수 선언 부분 ##
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:  # 첫 번째 노드 삽입
        node = Node(insert_data)
        node.link = head
        head = node
        return

    current = head
    while current.link != None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(insert_data)
            node.link = current
            pre.link = node
            return

    node = Node(insert_data)  # 마지막 노드 삽입
    current.link = node


def delete_nodes(delete_data):
    global head, current, pre

    print_nodes(head)
    if head.data == delete_data: # head 삭제
        print('첫 번째 노드 삭제 완료')
        current = head
        head = head.link
        del current
        return

    current = head  # current 증가
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            print('중간 노드 삭제 완료')
            pre.link = current.link
            del current
            print_nodes(head)
            return

    # 삭제할 데이터를 못찾은 경우엔 함수종료
    print('삭제할 노드를 찾지 못함')


def find_nodes(find_data):
    global head, current, pre

    current = head
    if current.data == find_data:
        return current

    while current.link != None:
        current = current.link
        if current.data == find_data:
            return current


## 전역 변수 선언 부분 ##
#memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]

## 메인 코드 부분 ##
if __name__ == "__main__":

    node = Node(data_array[0])  # 첫 번째 노드
    head = node
    #memory.append(node)

    for data in data_array[1:]:  # 두 번째 노드부터
        pre = node
        node = Node(data)
        pre.link = node
        #memory.append(node)

    print_nodes(head)
    insert_nodes("피카츄", "잠만보")
    print_nodes(head)
    insert_nodes("파이리", "어니부기")
    print_nodes(head)
    insert_nodes("성윤모", "거북왕")
    print_nodes(head)
    delete_nodes("잠만보")
    print_nodes(head)
    delete_nodes("어니부기")
    print_nodes(head)
    delete_nodes("강찬석")
    print_nodes(head)
