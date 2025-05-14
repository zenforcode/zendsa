from typing import List
def findDuplicate(nums: List[int]) -> int:
    slow,fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # find the netrance
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast
