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
        while currentNode != None and currentNode.data != target:
            prevNode = currentNode
            if target < currentNode.data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        # Case target has no children
        if currentNode.right == None and currentNode.left == None:
            if target < prevNode.data:
                prevNode.left = None
            else:
                prevNode.right = None

        # case target has one child
        elif currentNode.right != None or currentNode.left != None:
            if prevNode.left == currentNode:
                if currentNode.right != None:
                    prevNode.left = currentNode.right
                else:
                    prevNode.left = currentNode.left

            if prevNode.right == currentNode:
                if currentNode.right != None:
                    prevNode.right = currentNode.right
                else:
                    prevNode.right = currentNode.left

        # case target has two children
        elif currentNode.right != None and currentNode.left != None:
            rightNode = currentNode.right
            while rightNode.left != None:
                smallestNode = rightNode
                while smallestNode.left != None:
                    prevNode = smallestNode
                    smallestNode = smallestNode.right
            currentNode.data = smallestNode.data
            prevNode.left = None

    def preOrder(self, currentNode):
        if currentNode != None:
            print(currentNode.data)
            if currentNode.left != None:
                self.preOrder(currentNode.left)
            if currentNode.right != None:
                self.preOrder(currentNode.right)

    def inOrder(self, currentNode):
        if currentNode != None:
            print(currentNode.data)
            if currentNode.left != None:
                self.inOrder(currentNode.left)
            elif currentNode.right != None:
                self.inOrder(currentNode.right)





bt = BinaryTree()
bt.add(1)
bt.add(5)
bt.add(8)
bt.add(4)
bt.add(0)
bt.add(-3)

bt.preOrder(bt.start)

bt.delete(8)

bt.inOrder(bt.start)
