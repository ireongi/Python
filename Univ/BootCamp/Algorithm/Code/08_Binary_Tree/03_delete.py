## 함수 선언 부분 ##
class Tree_node():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역 변수 선언 부분 ##
memory = []
root = None
name_array = ['가', '나', '다', '라', '마', '바']

## 메인 코드 부분 ##
node = Tree_node()
node.data = name_array[0]
root = node
memory.append(node)

for name in name_array[1:]:

    node = Tree_node()
    node.data = name

    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

delete_name = '마마'

current = root
parent = None
while True:
    if delete_name == current.data:

        if current.left == None and current.right == None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del (current)

        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del (current)

        elif current.left == None and current.right != None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            del (current)

        print(delete_name, '이(가) 삭제됨.')
        break
    elif delete_name < current.data:
        if current.left == None:
            print(delete_name, '이(가) 트리에 없음')
            break
        parent = current
        current = current.left
    else:
        if current.right == None:
            print(delete_name, '이(가) 트리에 없음')
            break
        parent = current
        current = current.right
