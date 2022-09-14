#binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.start = None

    def add(self, data):
            newNode = Node(data)
            if self.start == None:
                self.start = newNode
            else:
                currentNode = self.start
                while currentNode != None:
                    prevNode = currentNode
                    if newNode.data < currentNode.data:
                        currentNode = currentNode.left
                    else:
                        currentNode = currentNode.right
                if newNode.data < prevNode.data:
                    prevNode.left = newNode
                else:
                    prevNode.right = newNode
                return True

    def delete(self, target):
        currentNode = self.start
        while currentNode != None and currentNode != target:
            prevNode = currentNode
            if target < currentNode.data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right


bt = BinaryTree()
print(bt.start)
bt.add(1)
print(bt.start.data)
bt.add(2)
print(bt.start.left)
