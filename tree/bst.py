from typing import TypeVar, List
from collections import deque
T = TypeVar('T')

class Node:
    def __init__(self, value: T) -> None:
        self.value = value
        self.right = None
        self.left = None
    def has_left_node(self) -> bool:
        return self.left is not None
    def has_right_node(self) -> bool:
        return self.right is not None
    
class Tree:
    def __init__(self, value: T) -> None:
        self._root = Node(value)

    def get_root(self) -> Node:
        return self._root

    def insert(self, value: T) -> Node:
        return self._insert_node(self._root, value)
    
    def insert_bst(self, value: T) -> None:
        if self._root is None:
            self._root = Node(value)
            return
        curr = self._root
        while curr:
            if value < curr.value:
                if curr.left is None:
                    curr.left = Node(value)
                    return 
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(value)
                    return 
                curr = curr.right

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

    def _insert_node(self, root: Node, value: T) -> Node:
        if root is None:
            return Node(value)
        
        q = deque([root])  # BFS queue
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

        return root  # Should never reach here

def pre_order(t: Tree) -> list[Node]:
    visited = []
    def traverse(node: Node):
        if node:
            visited.append(node.value)
            traverse(node.left)
            traverse(node.right)
    traverse(t.get_root())
    return visited 

def in_order(t: Tree) -> list[Node]:
    visited = []
    def traverse(node: Node):
        if node:
            traverse(node.left)
            visited.append(node)
            traverse(node.right)
    traverse(t.get_root())
    return visited

def post_order(t: Tree) -> list[Node]:
    visited = []
    def traverse(node: Node):
        if node:
            traverse(node.left)
            traverse(node.right)
            visited.append(node.value)
    traverse(t.get_root())
    return visited


def pre_order_using_stack(tree: T) -> List[T]:
    if not tree.get_root():
        return []
    
    visited = []
    stack = deque([tree.get_root()])  # Start with root node

    while stack:
        node = stack.pop()  # Process current node
        visited.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited

