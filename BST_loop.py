import random


class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):
        currentNode = self
        while True:
            if currentNode.value == None:
                currentNode.value == BST(value)
            elif value < currentNode.value:
                if currentNode.left == None:
                    currentNode.left = BST(value)
                    print(f'parent : {currentNode.value}')
                    print(f'left : {value}')
                    break
                else:
                    currentNode = currentNode.left
            elif value>currentNode.value:
                if currentNode.right == None:
                    currentNode.right = BST(value)
                    print(f'parent : {currentNode.value}')
                    print(f'right : {value}')
                    break
                else:
                    currentNode = currentNode.right
            elif value==currentNode.value:
                print('The Element already exists')
                break
            else:
                pass
        return self
    def contains(self,value):
        currentNode = self
        while True:
            if currentNode.value == value:
                return True
            elif currentNode.value > value:
                if currentNode.left != None:
                    currentNode = currentNode.left
                else:
                    return False
            elif currentNode.value < value:
                if currentNode.right != None:
                    currentNode = currentNode.right
                else:
                    return False
            elif currentNode.value == None:
                return False


tree = BST(2)
for i in range(1,10):
    tree.insert(random.randint(1,10))

print('Elements added')
# tree.tree_print()
