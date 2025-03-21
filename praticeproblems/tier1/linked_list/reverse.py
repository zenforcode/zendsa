from node import Node
from typing import TypeVar
T = TypeVar('T')

class LinkedList:
    def __init__(self)->None:
        self.head = None
    
def create_linked_list(arr: list[T]) -> LinkedList:
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    ll = LinkedList()
    ll.head = head
    return ll

def reverse_list(l: LinkedList) -> LinkedList:
    """
        Suppose the list is l = [0,1,2,3,4]
        1. prev = None current = (0)
        2. next_nodex = (1), current.next = None, prev = (0), current = (1) - removed 
        3. next_node = (2), current.next = (0), prev = (1), current = (2)  [1, 0, 2]
    """
    prev = None
    current = l.head    
    while current:
        next_node = current.next  
        current.next = prev 
        prev = current  
        current = next_node
    l.head = prev  
    return l

if __name__=="__main__":
    ll = create_linked_list([0,1,2,3,4])
    l = reverse_list(ll)
    current = l.head
    while current:
        print(current.data)
        current = current.next