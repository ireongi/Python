import random


## 함수 선언 부분 ##
class Tree_node():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def preorder(node):
    if not node:
        return
    print(node.data, end=' - ')  # current
    preorder(node.left)
    preorder(node.right)


## 전역 변수 선언 부분 ##
memory = []
root_book, root_auth = None, None
book_array = [['1', 'ㄱ'], ['2', 'ㄴ'], ['3', 'ㄷ'],
              ['4', 'ㄹ'], ['5', 'ㅁ'], ['6', 'ㅂ'],
              ['7', 'ㅅ'], ['8', 'ㅇ'], ['9', 'ㅈ']]
random.shuffle(book_array)

## 메인 코드 부분 ##

### 책 이름 트리 ###
node = Tree_node()
node.data = book_array[0][0]
root_book = node
memory.append(node)

for book in book_array[1:]:
    name = book[0]
    node = Tree_node()
    node.data = name

    current = root_book
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

print("숫자 트리 구성 완료!")

### 작가 이름 트리 ###
node = Tree_node()
node.data = book_array[0][1]
root_auth = node
memory.append(node)

for book in book_array[1:]:
    name = book[1]
    node = Tree_node()
    node.data = name

    current = root_auth
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

print("한글 트리 구성 완료!")

preorder(root_book)
print()

## 책 이름 및 작가 이름 검색 ##
bookOrAuth = int(input('숫자검색(1), 한글검색(2)-->'))
findName = input('검색할 숫자 또는 한글-->')

if bookOrAuth == 1:
    root = root_book
else:
    root = root_auth

current = root
while True:
    if findName == current.data:
        print(findName, '을(를) 찾음.')
        findYN = True
        break
    elif findName < current.data:
        if current.left == None:
            print(findName, '이(가) 목록에 없음')
            break
        current = current.left
    else:
        if current.right == None:
            print(findName, '이(가) 목록에 없음')
            break
        current = current.right
