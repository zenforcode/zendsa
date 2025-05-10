from typing import TypeVar, Optional

T = TypeVar('T')

class Node:
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Optional['Node'] = None

def create_linked_list(arr: list[T]) -> Optional[Node]:
    if not arr:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head: Optional[Node]) -> None:
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
