
#BASIC TREE

class Node:
    def __init__ (self,data):
        self.data= data
        self.left= None
        self.right = None



n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("left child node")

n1.left = n2
n1.right =n3

