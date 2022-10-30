class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree():
    def __init__ (self):
        self.root = None

tree = BinaryTree()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)
n9 = Node(90)


tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

#전위순회
# 10 20 40 80 50 30 60 70
def preorder(self, n):
    if n != None:
        print(n.item, '', end = '')
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)
tree.preorder(tree.root)