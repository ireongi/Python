## 함수 선언 부분 ##
class Tree_node():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역 변수 선언 부분 ##
memory = []
root = None
name_array = ['"가"', '"나"', '"다"', '"라"', '"마"', '"바"']

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

find_name = '"다"'

current = root
while True:
    if find_name == current.data:
        print('There is', find_name)
        break
    elif find_name < current.data:
        if current.left == None:
            print('There is NOT', find_name)
            break
        current = current.left
    else:
        if current.right == None:
            print('There is NOT', find_name)
            break
        current = current.right
