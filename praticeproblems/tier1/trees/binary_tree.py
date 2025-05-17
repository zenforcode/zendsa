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
        q = deque([self._root])
        while q:
            node = q.popleft()
            if not node.left:
                node.left = Node(value)
                return
            else:
                q.append(node.left)
            if not node.right:
                node.right = Node(value)
                return
            else:
                q.append(node.right)

    def delete(self, value: T) -> None:
        self._root = self._delete_node(self._root, value)

    def _delete_node(self, node: Optional[Node], value: T) -> Optional[Node]:
        if not node:
            return None

        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Node with two children: get the inorder successor (smallest in the right subtree)
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_node(node.right, min_larger_node.value)

        return node

    def _find_min(self, node: Node) -> Node:
        while node.left:
            node = node.left
        return node