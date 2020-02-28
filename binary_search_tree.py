from random import randint
class Node:
	def __init__(self,value = None):
		self.value = value
		self.left_child = None
		self.right_child = None

class Tree:
	def __init__(self):
		self.root = None	

	def insert(self,value):
		if self.root == None:
			self.root = Node(value)
		else:
			self._insert(self.root,value)
	def _insert(self,curr_node,value):
		if curr_node.value < value:
			if curr_node.right_child == None:
				curr_node.right_child = Node(value)
			else:
				self._insert(curr_node.right_child,value)

		elif curr_node.value > value:
			if curr_node.left_child == None:
				curr_node.left_child = Node(value)
			else:
				self._insert(curr_node.left_child,value)
		else:
			print("The value already exists")

	def print_tree(self):
		if self.root != None:
			print(self.root.value)
			self._print_tree(self.root)
	def _print_tree(self,curr_node):
		if curr_node != None:
			print(curr_node.value)
			self._print_tree(curr_node.left_child)
			self._print_tree(curr_node.right_child)

tree = Tree()
for i in range(1,20):
	tree.insert(randint(1,100))

tree.print_tree()