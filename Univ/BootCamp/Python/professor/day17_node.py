class Node:
	def __init__(self, data):
		self.left = None
		self.data = data
		self.right = None

	def __repr__(self):
		return f'{self.data}'


r = Node('피카츄')
print(r)