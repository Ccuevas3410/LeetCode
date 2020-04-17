class Node:
    def __init__ (self,data=None):
        self.data= data
        self.left= None
        self.right = None
        self.parent=None 



n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("left child node")

n1.left = n2
n1.right =n3




#BASIC BST 
class BST:
    def __init__(self):
        self.root_node = None

    def insert(self,data):
        if self.root_node is None:
            self.root_node = Node(data)

        else:
            self._insert(data,self.root_node)

    


    def _insert(self,data,currentNode):

      
        if data < currentNode.data :
            if currentNode.left is None:
                currentNode.left = Node(data)
            else:
                self._insert(data, currentNode.left)

        elif data > currentNode.data :

            if currentNode.right is None: 
                currentNode.right= Node(data)
            else:
                self._insert(data,currentNode.right)
        else:   
            print("VALUE IS ALREADY ON TREE")




    def search(self,data):
            if self.root_node is None:
                print("There is no nodes in the tree")
            else:
                self._search(data,self.root_node)


    def _search(self,data,currentNode):
            if currentNode is None:
                 print("Node not found")
            elif data < currentNode.data:
                self._search(data,currentNode.left)
            elif data > currentNode.data:
                self._search(data,currentNode.right)
            else:
                
                print("NODE FOUND")

            

    def printTree(self):
        if self.root_node!=None:
            self._printTree(self.root_node)

    
    def _printTree(self,currentNode):

        if currentNode!=None:
            print(currentNode.data)
            self._printTree(currentNode.left)  
            self._printTree(currentNode.right)
     

        

newTree = BST()
newTree.insert(15)
newTree.insert(16)
newTree.insert(14)

newTree.printTree()
newTree.search(15)
