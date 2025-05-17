# Sliding window.

Imagine you have a tray of 10 cookies and want to find the most chocolate chips in any 3 cookies next to each other. You must count the chips in every possible group of 3 cookies to do this. It might seem easy with just 10 cookies, but imagine doing the same when there are thousands or more. This can become time-consuming. We can avoid this hassle by using a smarter approach. Instead of recounting the chips for each group from scratch, you start by counting the chips in the first 3 cookies. Then, as you move to the next group, you simply subtract the chips from the cookie you leave behind and add the chips from the new cookie you include. This way, you quickly check each group without starting over every time. This smart technique is called the sliding window pattern.

The sliding window pattern is a technique for efficiently processing sequential data, such as arrays and strings. It involves maintaining a dynamic window that slides across the data, allowing you to examine a fixed portion at a time. Instead of repeatedly scanning the entire dataset, this approach adjusts the window’s boundaries as needed to track relevant elements. It is especially useful for solving problems involving contiguous subarrays or substrings, such as finding the maximum sum of a subarray or detecting repeated patterns in a string. This pattern can be viewed as a variation of the two-pointer approach, where the pointers define the window’s start and end.

Depending on the problem, the sliding window can be of a fixed size or dynamic.

- The fixed-size window is used when the window size is given or constant. For example, find the largest sum of any three consecutive numbers.
- The dynamic window is used when the window size changes based on conditions. For example, find the smallest subarray whose sum exceeds a target.

```python
def slidingWindow(arr, k, processWindow):
  # Initialize the window result (sum, product, count, etc.)
  windowResult = INITIAL_VALUE
  
  # Compute the initial window's result
  for i in range(k):
    updateWindowResult(arr)

  # Process the first window
  processWindow(windowResult)

  # Slide the window across the array
   for i in range(k, len(arr)-1):
    updateWindowResultByAdding(arr[i]) # add a new element to the window
    updateWindowResultByRemoving(arr[i-j]) # remove outgoing element
    processWindow(windowResult)  # Operation on the updated window
```

There is a very common group of problems involving subarrays that can be solved efficiently with sliding window. Let's talk about how to identify these problems.

First, the problem will either explicitly or implicitly define criteria that make a subarray "valid". There are 2 components regarding what makes a subarray valid:

1. A constraint metric. This is some attribute of a subarray. It could be the sum, the number of unique elements, the frequency of a specific element, or any other attribute.
2. A numeric restriction on the constraint metric. This is what the constraint metric should be for a subarray to be considered valid.

Second, the problem will ask you to find valid subarrays in some way.

1. The most common task you will see is finding the best valid subarray. The problem will define what makes a subarray better than another. For example, a problem might ask you to find the longest valid subarray.
2. Another common task is finding the number of valid subarrays. 

## Requirements for a sliding window problem

For sure we're ahead a sliding window problem when:

1. Contiguous data: The input data is stored in a contiguous manner, such as an array or string.
2. Processing subsets of elements: The problem requires repeated computations on a contiguous subset of data elements (a subarray or a substring), such that the window moves across the input array from one end to the other. The size of the window may be fixed or variable, depending on the requirements of the problem.
3. Efficient computation time complexity: The computations performed every time the window moves take constant or very small time.


So ask your self:
1. The data is contiguous? (string/array)
2.  The processing sub


For example
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

It might look like a sliding window problem. But it is not a classic sliding window problem due to: 
- All elements are non-negative (e.g. positive integers or 0).
- You want to maintain a contiguous window of elements where the sum or another property fits a constraint.
- You can expand or shrink the window based on comparisons like sum > k or sum < k.

#### Why This Is NOT a Sliding Window Problem:

    1. The array can contain negative numbers.
        With negative numbers, increasing the window size doesn't necessarily increase the sum, and shrinking it doesn't necessarily decrease it. So you can't deterministically adjust the window left/right based on sum comparisons.
    2. You need to count all subarrays that sum to k.

        This means you have to consider every possible subarray — not just the longest or shortest one that meets a condition.
        Sliding window is typically used for finding a window that meets a constraint, not counting all that do.
