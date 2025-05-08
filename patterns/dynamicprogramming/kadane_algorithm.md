## Kadane Algorithms

Kadane Algorithm is dynamic programming problem:

```python
def maxSubarraySum(nums):
    if not nums:
        return 0
    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global
```

In DP, we solve a problem by breaking it down into subproblems, solving each subproblem once, and using the results to build up solutions to larger problems.

For the maximum subarray sum:
We define a DP state:
   dp[i] = the maximum subarray sum ending at index i
   dp[i] = max(nums[i], dp[i - 1] + nums[i])

This means:

- Either start a new subarray at i (just nums[i])
- Or extend the previous subarray (dp[i - 1] + nums[i])

Kadane’s Algorithm is a space-optimized version of this:
Instead of storing an entire dp[] array, it just keeps track of:
- max_current (dp[i])
- max_global (maximum of all dp[i] so far)
So yes—Kadane's Algorithm is a DP approach with O(1) space.