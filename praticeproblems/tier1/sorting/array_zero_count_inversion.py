""""
You are give an array of n positive intergers a1,a2,...,an
In one operation you can do the following:
1. choose any integer x
2. for all i sich ai = x do a = 0

find the minimum of operations required to sort in decreasing order.
# input format
the first line contains n - lenght of the array
the second line contains n integers a1... an.
# Output format.
the minumun number of operation to sort in decreasing order.
"""

def count_inversion_helper(arr:list[int], lower:int, higher:int) -> tuple[int, int]:
  pivot = arr[higher]
  i = lower
  count = 0
  for j in range(lower, higher):
    if arr[j] <= pivot:
       count+=1
       k = arr[i]
       v = arr[j]
       print(f"Swap: {k} {v}")
       arr[i], arr[j] = arr[j], arr[i]
       i+=1 
  k = arr[i]
  v = arr[higher]
  print(f"Swap: {k} {v}")
  arr[i], arr[higher] = arr[higher], arr[i]
  return count+1, i 

def count_inversion(arr:list[int], lo:int, hi:int) -> int:
    if lo >= hi or lo < 0:
        return 0
    partition_count, pivot = count_inversion_helper(arr, lo, hi)
    partition_count+=count_inversion(arr, lo, pivot-1)
    partition_count+=count_inversion(arr,pivot+1,hi)
    return partition_count

def move_to_begin(arr, x):
    writer, reader = -1, 0
    while reader < len(arr):
        if arr[reader] == x:
            arr[reader],arr[writer] = arr[writer],arr[reader]
            arr[writer] = 0
            writer+=1
        reader+=1
    return writer
    
def min_order_sort(arr: list[int], x: int) -> int:
    start = move_to_begin(arr, x)
    if start == len(arr) -1:
        return 0
    count = count_inversion(arr, start+1, len(arr)-1)
    print(arr)
    return count

if __name__=="__main__":
    arr = [5,1,2,0,8,4]
    print(min_order_sort(arr, 3))



   