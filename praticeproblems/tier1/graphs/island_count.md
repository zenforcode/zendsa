## Problem: Counting Island

Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual "corner" (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.

```python
binaryMatrix = [ [0,    1,    0,    1,    0],
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1] ]

count_island(binaryMatrix)
output: 6 # since this is the number of islands in binaryMatrix.
          # See all 6 islands color-coded below.
```
## Solution

To solve the problem of counting the number of islands in a 2D binary matrix, we can use Depth-First Search (DFS) or Breadth-First Search (BFS) to traverse each group (or "island") of 1s. When we find a 1, we start a DFS/BFS to mark all connected 1s as visited and increment our island counter.

We'll use DFS here as it's intuitive and can be implemented recursively.

✅ Key Concepts
Adjacency is only in four directions: up, down, left, right (not diagonals).
We'll mutate the input matrix or maintain a visited set to avoid revisiting nodes.
Each time we find an unvisited 1, it represents a new island, and we perform a DFS from there to mark the entire island.
✅ Time and Space Complexity
Time Complexity: O(m * n)
We visit each cell at most once.

Space Complexity: O(m * n) in worst case due to:

Recursion stack in DFS (in case of one big island),
Or the visited set (if used).