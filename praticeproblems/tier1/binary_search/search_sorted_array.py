"""
Given a sorted array of intergers arr, and a target value, return the target's index 
if it exists int he array or -1 if it doesn't.
```
arr = [-2,0,3,4,7,9,11], target = 0
output --> 2
```
"""
def sorted_search_array(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

