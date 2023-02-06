## 클래스와 함수 선언 부분 ##
class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def find_node(find_data):
    global memory, head, current, pre

    current = head
    if current.data == find_data:
        print("First node")
        return current
    while current.link != head:
        current = current.link
        if current.data == find_data:
            print("Middle node")
            return current
    print("Nothing")
    return Node()  # 빈 노드 반환


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
data_array = ["가", "나", "다", "라", "마"]

## 메인 코드 부분 ##
if __name__ == "__main__":

    node = Node()  # 첫 번째 노드
    node.data = data_array[0]
    head = node
    node.link = head
    memory.append(node)

    for data in data_array[1:]:  # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    print_nodes(head)

    fNode = find_node("가")
    print(fNode.data)

    fNode = find_node("나")
    print(fNode.data)

    fNode = find_node("C")
    print(fNode.data)
