from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None

class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None

def create_linked_list(arr: list[T]) -> LinkedList[T]:
    ll = LinkedList[T]()
    if not arr:
        return ll  # Return empty LinkedList
    ll.head = Node(arr[0])
    current = ll.head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return ll

def reverse_list(l: LinkedList[T]) -> LinkedList[T]:
    prev = None
    current = l.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    l.head = prev
    return l

if __name__ == "__main__":
    ll = create_linked_list([0, 1, 2, 3, 4])
    reversed_ll = reverse_list(ll)
    current = reversed_ll.head
    while current:
        print(current.data)
        current = current.next
