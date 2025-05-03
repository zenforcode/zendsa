from collections import deque
from typing import Optional, TypeVar

T = TypeVar("T")

class Node:
    def __init__(self, value: T) -> None:
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

class BinaryTree:
    def __init__(self, value: T) -> None:
        self._root = Node(value)

    def get_root(self) -> Node:
        return self._root
    
    def insert(self, value: T) -> None:
        self._insert_node(self._root, Node(value))
    
    def delete(self, value: T) -> Optional[Node]:
       if self._root is None:
           return None
    def _delete_node(self, x: Node, value: T):
        if x is None:
            return None
        if x.value < value:
            self._delete_node(x.left, value)
        elif x.value > value:
            self._delete_node(x.right, value)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            # compute the min
            t = x.right
            stack = deque([t])
            min_value = None
            while stack:
                min_value = stack.pop()
                if min_value.left:
                    stack.append(min_value.left)
                    
                




    def _insert_node(self, root: Node, value: T) -> Node:
        if root is None:
            return Node(value)
        q = deque([root])  
        while q:
            curr: Node = q.popleft()            
            if curr.left is None:
                curr.left = Node(value)
                return root
            else:
                q.append(curr.left)

            if curr.right is None:
                curr.right = Node(value)
                return root
            else:
                q.append(curr.right)

        return root  


