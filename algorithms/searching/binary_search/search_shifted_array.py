from typing import List
from math import floor

def find_pivot_point(arr: List[int]) -> int:
    begin, end = 0, len(arr) - 1
    while begin < end:
        mid = begin + (end - begin) // 2
        if arr[mid] > arr[end]:
            begin = mid + 1
        else:
            end = mid
    return begin

def binary_search(arr: List[int], start: int, end: int, num: int) -> int:
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def shifted_arr_search(shiftArr: List[int], num: int) -> int:
    if not shiftArr:
        return -1

    pivot = find_pivot_point(shiftArr)
    if shiftArr[pivot] <= num <= shiftArr[-1]:
        return binary_search(shiftArr, pivot, len(shiftArr) - 1, num)
    else:
        return binary_search(shiftArr, 0, pivot - 1, num)

# Example usage
print(shifted_arr_search([4,5,6,7,0,1,2], 0))  # Output: 4

