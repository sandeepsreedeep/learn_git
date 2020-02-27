class Node():
	def __init__(self,value):
		self.value = value
		self.right_child = None
		self.left_child = None

class Tree():
	def __init__(self):
		self.root = Node()

	def insert(self,value):
		if self.root == None:
			self.root = Node(val)
		else:
			self._insert(val,self.root)
	def _insert(self,value,cur_node):
		if value<self.cur_node.value:
			if cur_node.left_child == None:
				cur_node.left_child = Node(value)
			else:
				self._insert(value,cur_node)
		elif value>self.cur_node.value:
			if cur_node.right_child == None:
				cur_node.right_child = Node(value)
			else:
				self._insert(value,cur_node)


tree = Tree()
