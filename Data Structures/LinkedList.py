class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def addToHead(self, info):

        if self.head is None:
            self.head = Node(info)

        else:
            temp = Node(info)
            temp.next = self.head
            self.head = temp

    def append(self, info):
        
        curr = self.head
        if curr :
            ##WE USE WHILE CURR.NEXT BECAUSE WE DO  CARE ABOUT NEXT NODE TO KNOW WHERE TO APPEND
            while curr.next:
                curr = curr.next
            curr.next = Node(info)
        else:
            self.head = Node(info)
         

    def print(self):
        curr = self.head

        ##WE USE WHILE CURR BECAUSE WE DO NOT CARE ABOUT NEXT TO PRINT THE NODE RIGHT NOW
        while curr:
            print(curr.data)
            curr = curr.next

    def delete(self,info):

        curr = self.head

        if self.head.data == info:
            self.head = self.head.next
        else:

            while curr.next.data != info:
                curr = curr.next
                print("HERE")

        curr.next = curr.next.next
        


list = SinglyLinkedList()
list.append(30)
list.append(2354)
list.addToHead(11)

print("NEW APPEND")
list.append(35)
list.addToHead(15)
list.print()
list.delete(15)


print("NEW LIST")
list.print()
