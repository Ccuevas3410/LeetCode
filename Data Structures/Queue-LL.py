class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def queue(self,value):
        curr = self.head
        

        if curr:
            ##WE USE WHILE CURR.NEXT BECAUSE WE DO  CARE ABOUT NEXT NODE TO KNOW WHERE TO APPEND
            while curr.next:
                curr = curr.next
            curr.next = Node(value)
        else:
            self.head = Node(value)
            
    def enqueue(self):
        curr = self.head
        if curr:
            ##WE USE WHILE CURR.NEXT BECAUSE WE DO  CARE ABOUT NEXT NODE TO KNOW WHERE TO APPEND
            self.head= self.head.next
        else:
            print("No values do enqueue")

    def print(self):
        curr = self.head

        if curr is not None:
         while curr:
            print(curr.data)
            curr = curr.next
        else:
            print("Stack is empty")


q = Queue()
q.queue(10)
q.queue(20)
q.queue(30)
q.enqueue()
q.print()