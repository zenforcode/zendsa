
# Mastering Backtracking in Python: Concepts and LeetCode Examples

Backtracking is a fundamental algorithmic technique used in computer science to solve problems by exploring all possible options and abandoning paths that fail to meet the criteria. It’s especially powerful in solving puzzles, generating combinations or permutations, and finding feasible paths through complex search spaces.

In this post, we’ll dive deep into backtracking in Python, look at its recursive and iterative forms, and apply it to two classic LeetCode problems.

---

## 🌱 What Is Backtracking?

Backtracking is a technique that **builds potential solutions step by step**, and **reverts (backtracks)** when a path doesn’t lead to a valid outcome. The process generally follows three steps:

1. **Explore:** Make a choice and move forward.
2. **Backtrack:** Undo the last choice.
3. **Explore next:** Try another possibility.

### When Do We Use It?

Backtracking is ideal for:
- Generating permutations or combinations
- Solving constraint satisfaction problems (e.g., Sudoku)
- Pathfinding in grids or graphs

---

## 🔍 Why Backtracking?

While backtracking may seem brute-force, its ability to **prune infeasible paths** makes it efficient in many practical cases. It’s often the most intuitive and straightforward approach to explore all possible configurations.

---

## 🔢 LeetCode 46 — Permutations (Recursive Backtracking)

Given a list of distinct integers, return all possible permutations.

### Python Code:

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, [], set(), result)
        return result

    def backtrack(self, nums, current, used, result):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for num in nums:
            if num in used:
                continue
            current.append(num)
            used.add(num)
            self.backtrack(nums, current, used, result)
            current.pop()
            used.remove(num)
```

### 🔑 Key Concepts:
- **Base Case:** When current permutation is complete
- **Backtrack:** After exploring one path, remove the last number and try the next

---

## 🎯 LeetCode 39 — Combination Sum (Recursive Backtracking)

Return all combinations of candidates that sum up to the target. Each number may be used unlimited times.

### Python Code:

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result

    def backtrack(self, candidates, target, start, current, result):
        if target == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            current.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, current, result)
            current.pop()
```

---

## 🔁 Iterative Backtracking (DFS-style)

Instead of recursion, we can simulate the call stack manually.

### Permutations Iteratively:

```python
def permute(nums: List[int]) -> List[List[int]]:
    result = []
    stack = [([], set())]

    while stack:
        current, used = stack.pop()
        if len(current) == len(nums):
            result.append(current)
            continue
        for num in nums:
            if num in used:
                continue
            stack.append((current + [num], used | {num}))
    return result
```

### Combination Sum Iteratively:

```python
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    stack = [([], target, 0)]

    while stack:
        current, remaining, index = stack.pop()
        if remaining == 0:
            result.append(current)
            continue
        for i in range(index, len(candidates)):
            if candidates[i] > remaining:
                continue
            stack.append((current + [candidates[i]], remaining - candidates[i], i))
    return result
```

---

## 📊 Recursive vs Iterative: Which One?

| Criteria              | Recursive              | Iterative                   |
|-----------------------|------------------------|-----------------------------|
| Readability           | ✅ More intuitive       | ❌ More verbose             |
| Stack depth           | ❌ May cause overflow   | ✅ More scalable            |
| Debuggability         | ❌ Implicit state       | ✅ Explicit state           |
| Flexibility           | ✅ Simple state passing | ✅ Fine-grained control     |

---

## 🧠 More Backtracking Problems to Practice

- **78. Subsets**
- **90. Subsets II**
- **131. Palindrome Partitioning**
- **79. Word Search**
- **51. N-Queens**
- **52. N-Queens II**

---

## 🧩 Conclusion

Backtracking is a powerful, elegant technique for solving a wide range of problems that require exploring multiple paths. Whether using recursion or an iterative simulation of it, understanding how to **explore, backtrack, and explore alternatives** is key.

Practice is essential—once you master backtracking, you’ll be equipped to solve many of the trickiest algorithm problems out there.

---
