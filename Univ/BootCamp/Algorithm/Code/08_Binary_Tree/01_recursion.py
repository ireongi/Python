class Tree_node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


node1 = Tree_node()
node1.data = '1층'

node2 = Tree_node()
node2.data = '2_1층'
node1.left = node2

node3 = Tree_node()
node3.data = '2_2층'
node1.right = node3

node4 = Tree_node()
node4.data = '3_1층'
node2.left = node4

node5 = Tree_node()
node5.data = '3_2층'
node2.right = node5

node6 = Tree_node()
node6.data = '3_3층'
node3.left = node6


def preorder(node):
    if node == None:
        return
    print(node.data, end=' - ')  # current
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end=' - ')  # current
    inorder(node.right)


def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' - ')  # current


print('Preorder Traversal : ', end='')
preorder(node1)
print('끝')

print('Inorder Traversal : ', end='')
inorder(node1)
print('끝')

print('Post Traversal : ', end='')
postorder(node1)
print('끝')
