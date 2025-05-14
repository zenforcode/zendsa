# Fast and Slow Pointers (Hare and Tortoise) — Simplified Explanation
The fast and slow pointers pattern is a technique that uses two pointers moving at different speeds to efficiently solve problems involving cycles, midpoints, or intersections in data structures like linked lists or arrays.

1. Slow pointer (Tortoise) moves one step at a time.

2. Fast pointer (Hare) moves two steps at a time.

This approach is especially useful when you need to:

- Detect if there's a cycle in a linked list.
- Find the middle of a linked list.
- Detect intersection points or duplicates.

## Key Insight
If there is a cycle, the fast pointer will eventually “lap” the slow pointer — just like two runners on a circular track, where the faster one eventually catches up to the slower one.

### Simple Analogy
Imagine two people running on a circular track. If one runs twice as fast as the other, they’ll eventually meet again, even if they started together. This is exactly how the cycle detection works.

### Simple Example: Detecting a Cycle in a Linked List

**Problem: Given a linked list, determine if it contains a cycle.**

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next         # Move 1 step
        fast = fast.next.next    # Move 2 steps

        if slow == fast:
            return True          # Cycle detected

    return False                 # No cycle
```
#### How It Works:
Both pointers start at the head.

- The slow pointer moves one node at a time.
- The fast pointer moves two nodes at a time.
If the list has a cycle, the fast pointer will eventually catch up to the slow pointer.
If the list ends (fast reaches None), there's no cycle.

#### Use Cases:
- Cycle detection (e.g., in Floyd’s Cycle Detection Algorithm)
- Finding the middle of a list
- Checking for duplicates in a sequence (e.g., Floyd’s algorithm for finding repeated numbers)
