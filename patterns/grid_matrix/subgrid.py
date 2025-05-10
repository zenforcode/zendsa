
"""
Given a rectangular grid of integers with dimensions R×C (where R > 0 and C > 0), return a new grid of the same size where each cell [r][c] contains the maximum value within the subgrid starting at [r][c] (top-left) and ending at [R-1][C-1] (bottom-right).
0 k = r[R-1][C-1], k-->2

## STEP A
1. read the statement twice 
2. work though examples
3. find corner cases
4. clarify questions: input/output format, questions contrains (rxc)
## STEP B
Naive Solution:
    1. find the max(i, j) and compare with current value x value.
Better Solution:
 Built up the matrix starting from the bottom and always look the left and the bottom
grid = [
    [1, 5, 3],
    [4, -1, 0],
    [2, 0, 2]
]


1. grid = [
    [1, 5, 3],
    [4, -1, 0],
    [2, 2, 2]
]
"""
from typing import List
def find_subgrid_max(grid: List[List[int]]) -> List[List[int]]:
    R = len(grid)
    C = len(grid[0])
    dp = [[0] * C for _ in range(R)]
    dp[R - 1][C - 1] = grid[R - 1][C - 1]
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if r == R - 1 and c == C - 1:
                continue
            compare = [grid[r][c]]
            if r + 1 < R:
                compare.append(dp[r + 1][c])
            if c + 1 < C:
                compare.append(dp[r][c + 1])
            dp[r][c] = max(compare)
    for row in dp:
        print(row)

    return dp


# Example input
input_grid = [
    [1,  5, 3],
    [4, -1, 0],
    [2,  0, 2]
]

find_subgrid_max(input_grid)
