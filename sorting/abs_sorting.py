from typing import List

def absSort(arr: List[int]) -> List[int]:
    def compare(x, y):
        if abs(x) < abs(y):
            return True
        elif abs(x) > abs(y):
            return False
        return x < y

    def quicksort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if compare(arr[j], pivot):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(0, len(arr) - 1)
    return arr

