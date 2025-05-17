## Prefix sum

Motivating Problem:

*Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.*

## Definition of Prefix Sum

Given an array A, the prefix sum array P is defined as:

``
P[0] = A[0]
P[1] = A[0] + A[1]
P[2] = A[0] + A[1] + A[2]
...
P[i] = A[0] + A[1] + ... + A[i]
``
To find the sum of elements between index i and j in the array A, we use:

``
sum(i to j) = P[j] - P[i - 1]  if i > 0
sum(0 to j) = P[j]            if i == 0
``
### Example
Let’s use your array:
```python
A = [-2, 1, 2, -2, 5, -2, 1]
```
Let’s compute its prefix sum P:

text
Copy
Edit
Index:     0   1   2   3   4   5   6
Value:    -2  +1  +2  -2  +5  -2  +1
Prefix:  [-2, -1,  1, -1,  4,  2,  3]
### Q1: What is the sum of A[0:2]? (Subarray [-2, 1, 2])
Use P[2] = 1 (which is correct)
Since i = 0, sum = P[2] = 1

### What is the sum from index 2 to 6? ([2, -2, 5, -2, 1])
We want sum = A[2] + A[3] + A[4] + A[5] + A[6] = 4

Using prefix sums: sum = P[6] - P[1] = 3 - (-1) = 4
###  Important Clarification
"The last index of the prefix sum gives us 3. Our sum is 4."
This confusion happens when you forget to subtract the prefix sum before the start index of your subarray.

The rule is:


If you don’t subtract P[i - 1], you get the total from index 0, not just from i.

| Subarray           | i | j | PrefixSum[j] | PrefixSum[i-1] | Sum(i to j) = P[j] - P[i-1] |
|--------------------|---|---|------        |--------|------------------------------|
| [-2, 1, 2]         | 0 | 2 |  1           |   —    | 1                            |
| [2, -2, 5, -2, 1]  | 2 | 6 |  3           |  -1    | 3 - (-1) = 4                 |

Sum(nums[2,6]) = P[6] - P[2 -1] = 4
So we've seen that to find the number from i to j inclusive we've:
Sum([i, j]) = PrefixSum[j] - PrefixSum[i - 1] (only if i > 0)

