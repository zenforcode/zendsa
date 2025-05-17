## Prefix Sum

### Motivating Problem

*Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.*

> A **subarray** is a contiguous non-empty sequence of elements within an array.

---

## Definition of Prefix Sum

Given an array `A`, the prefix sum array `P` is defined as:

```
P[0] = A[0]
P[1] = A[0] + A[1]
P[2] = A[0] + A[1] + A[2]
...
P[i] = A[0] + A[1] + ... + A[i]
```

To find the sum of elements between index `i` and `j` in the array `A`, we use:

```
sum(i to j) = P[j] - P[i - 1]  if i > 0
sum(0 to j) = P[j]            if i == 0
```

---

## Example

Let’s use the array:
```python
A = [-2, 1, 2, -2, 5, -2, 1]
```

We compute its prefix sum `P`:

```
Index:     0   1   2   3   4   5   6
Value:    -2  +1  +2  -2  +5  -2  +1
Prefix:  [-2, -1,  1, -1,  4,  2,  3]
```

---

### Q1: What is the sum of `A[0:2]`?  
Subarray: `[-2, 1, 2]`  
- `P[2] = 1`  
- Since `i = 0`, sum = `P[2] = 1` ✅

---

### Q2: What is the sum from index 2 to 6?  
Subarray: `[2, -2, 5, -2, 1]`  
- We want `sum = A[2] + A[3] + A[4] + A[5] + A[6] = 4`  
- Using prefix sums: `sum = P[6] - P[1] = 3 - (-1) = 4` ✅

---

## Important Clarification

> *"The last index of the prefix sum gives us 3. Our sum is 4."*

This confusion happens when you forget to subtract the prefix sum **before** the start index of your subarray.

### Rule Reminder:

- If `i > 0`: `sum(i to j) = P[j] - P[i - 1]`
- If `i == 0`: `sum(i to j) = P[j]`

If you don’t subtract `P[i - 1]`, you are calculating the total sum from index 0 to `j`, not just from `i`.

---

## Visual Summary

| Subarray           | i | j | PrefixSum[j] | PrefixSum[i-1] | Sum(i to j) = P[j] - P[i-1] |
|--------------------|---|---|---------------|----------------|-----------------------------|
| [-2, 1, 2]         | 0 | 2 | 1             | —              | 1                           |
| [2, -2, 5, -2, 1]  | 2 | 6 | 3             | -1             | 3 - (-1) = 4                |

Thus:
```
Sum(nums[2:6]) = P[6] - P[1] = 4
```

---

## Final Insight

To find the sum from index `i` to `j` (inclusive), use:

```
Sum([i, j]) = PrefixSum[j] - PrefixSum[i - 1]   if i > 0
```

This concept is fundamental for solving:

> **"Find the number of subarrays whose sum equals `k`."**

so 
```
(*) k = PrefixSum[j] - PrefixSum[i - 1]   if i > 0
```

```
PrefixSum[i - 1] = PrefixSum[j] - k
```

Let’s say the prefix sums (as we traverse the array) are:

[-2, -1, 1, -1, 4, 2, 3]

where the array is:
[-2, 1, 2, -2, 5, -2, 1]

We're keeping track of previously seen prefix sums using a hash map (prefix_sums) that counts their frequency.

## Step-by-step:
1. Prefix sum = -2
- Check if -2 - 3 = -5 exists in prefix_sums -> No
- No subarray found here.

2. Prefix sum = -1
- Check if -1 - 3 = -4 exists → ❌ No
- Still no subarray found.

3. Prefix sum = 1
- Check if 1 - 3 = -2 exists → ✅ Yes!
- prefix_sums[-2] = 1, so we found 1 valid subarray → count += 1

4. Prefix sum = -1
- Check if -1 - 3 = -4 exists → ❌ No
- No new subarrays here.

5. Prefix sum = 4
- Check if 4 - 3 = 1 exists → ✅ Yes!
- prefix_sums[1] = 1, so count += 1

6. Prefix sum = 2
-  Check if 2 - 3 = -1 exists → ✅ Yes!
- prefix_sums[-1] = 2 (we’ve seen -1 twice)
- So add 2 to count → count += 2
- Now count = 4

- Prefix sum = 3
 - Check if 3 - 3 = 0 exists
-  No update to count. but wait...we've a zero at very start so we can increase +1

- Final Count = 5
These represent the number of subarrays with sum exactly equal to k = 3.

```python
from typing import List, Dict
    def subarraySum(self, nums: List[int], k: int) -> int:
        count: Dict[int,int] = defaultdict(int) # we use this for keeping the frequency all set to zero
        count[0] = 1  # frequency of 1
        prefix_sum: int = 0
        count: int = 0
        answer: int = 0        
        for num in nums:
            # update the prefix sum
            prefix_sum+= num
            # is already in the hashmap if not we add zero
            answer += count.get([current_sum - k], 0)
            count[prefix_sum] = count.get(prefix_sum,0) + 1        
        return answer

```




