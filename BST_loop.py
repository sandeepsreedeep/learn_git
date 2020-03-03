import random
class Node(value):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        currentNode = self
        if currentNode.root == None:
            currentNode.root == Node(value)
        elif value < currentNode.root:
            if currentNode.left == None:
                currentNode.left = Node(value)
                break
            else:
                currentNode = currentNode.left
        elif value>currentNode.root:
            if currentNode.right == None:
                currentNode.right = Node(value)
                break
            else:
                currentNode = currentNode.right
