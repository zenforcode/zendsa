from typing import Optional
class LinkedList:
    value: int
    next: Optional['LinkedList']

def has_cycle(head):
    slow = head
    fast = head
    if head is None:
        return False

    while fast and fast.next:
        slow = slow.next         
        fast = fast.next.next    

        if slow == fast:
            return True          

    return False                 
