
from typing import Optional
class ListNode:
    def __init__(self, val:int =0, next:'ListNode'=None):
         self.val: int = val
         self.next: 'ListNode' = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    if head.next is None:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
