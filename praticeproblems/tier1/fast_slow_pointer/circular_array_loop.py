from typing import List

def next_step(pointer, value, size):
    return (pointer + value) % size
def is_not_cycle(nums, start_direction, pointer):
    curr_direction = nums[pointer] >= 0
    if (start_direction != curr_direction) or (nums[pointer] % len(nums) == 0):
        return True
    else:
        return False
    
def circularArrayLoop(nums):  
    n = len(nums)
    for idx in range(n):
        forward = nums[idx] > 0 # forward
        slow, fast = idx, idx
        while True:
            slow = next_step(slow, nums[slow], n) 
            if is_not_cycle(nums, forward, slow):
                break
            fast = next_step(fast, nums[fast], n)
            if is_not_cycle(nums, forward, fast):
                break                
            fast = next_step(fast, nums[fast], n)
            if is_not_cycle(nums, forward, fast):
                break
            if slow == fast:
                return True
    return False
