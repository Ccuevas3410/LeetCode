 def oddEvenList(head):
        
        odd = head
        even = head.next
        evenHead = even
        
        
        while (odd and even and  odd.next and even.next ):
            odd.next= even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
            


