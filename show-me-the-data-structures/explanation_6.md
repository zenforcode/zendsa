
## Union Function
The goal is to do set union between two linked list.
### Reasoning Behind Decisions:

There are several approaches to merge two linked lists while ensuring uniqueness:

Let N = size of the fist list.
Let M = size of the second list.

1. Merge Sort Approach
    Initially considered Merge Sort, but its complexity would be O(N log N + M log M) + O(N + M) (sorting both lists and merging).
    This is suboptimal for maintaining uniqueness.

2. Optimal Approach: Using a HashSet (Python set)
    A set provides O(1) average-time complexity for insertions and lookups.
    The idea:
        1. Traverse the first linked list, add elements to both the set and the output list.
        2. Traverse the second linked list, check if the element is in the set, and if not, add it to the output list.

This ensures O(N + M) time complexity, making it the most efficient method.

### Time Efficiency:

Let N = size of the fist list.
Let M = size of the second list.

- O(N+M). We must visit every elements.

### Space Efficiency:

Let N = size of the first list.
Let M = size of the second list.
Let K = unique elements
- O(N) for the set.
- O(K) for the output list

O(N+K) is the space complexity. It is a linear complexity.

## Intersection Function
In this case since the list are not ordered we need two hashset. Ordering the list will add time overhead.
### Reasoning Behind Decisions:
So we copy each list in the set and the we intersect the list

### Time Efficiency:
Let N = size of the first list.
Let M = size of the second list.
O(N+M) we need to visit both lists to copy the values into the set and then intersect.
### Space Efficiency:
Let N = size of the first list.
Let M = size of the second list.
O(N+M) we need to store values in the sets and then intersect to create a list that is < N+M
