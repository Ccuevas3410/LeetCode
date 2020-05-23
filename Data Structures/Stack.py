


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__ (self):
        self.head = None

    def push(self,data):
        
        curr = self.head
        if curr:
            
            temp = Node(data)
            temp.next= self.head
            self.head = temp

        else:
            self.head = Node(data)
    
    def print(self):
        curr = self.head

        if curr is not None:
         while curr:
            print(curr.data)
            curr = curr.next
        else:
            print("Stack is empty")

    def pop(self):
        curr = self.head

        if curr is not None:
            self.head = self.head.next
            return curr.data

        else:
         print ("Stack is empty, pop not allowed")
    

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.print()
s.pop()
print("NEW STAACK")
s.print()