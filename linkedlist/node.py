from typing import TypeVar
T = TypeVar('T')
class Node:
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None

def create_linked_list(arr: list[T]) -> Node:
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head: Node):
    while head:
        print(head.data, end=" ")
        head = head.next
    print(" ")