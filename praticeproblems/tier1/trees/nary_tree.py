from collections import deque
from typing import List, Optional, TypeVar

T = TypeVar("T")

class Node:
    def __init__(self, value: T) -> None:
        self.value = value
        self.children: List["Node"] = []

class NaryTree:
    def __init__(self, value: T, max_children: int) -> None:
        self._root = Node(value)
        self._max_children = max_children

    def get_root(self) -> Node:
        return self._root

    def insert(self, value: T) -> None:
        new_node = Node(value)
        queue = deque([self._root])
        while queue:
            current = queue.popleft()
            if len(current.children) < self._max_children:
                current.children.append(new_node)
                return
            queue.extend(current.children)

    def delete(self, value: T) -> None:
        if self._root.value == value:
            self._root = None 
            return

        queue = deque([self._root])
        while queue:
            current = queue.popleft()
            for i, child in enumerate(current.children):
                if child.value == value:
                    current.children.pop(i)
                    return
                queue.append(child)

    def traverse_level_order(self) -> List[T]:
        if not self._root:
            return []

        result = []
        queue = deque([self._root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            queue.extend(node.children)
        return result
