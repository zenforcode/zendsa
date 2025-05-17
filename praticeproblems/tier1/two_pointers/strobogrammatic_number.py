class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}        
        left = 0 
        right = len(num) - 1
        while left <= right:
            if num[left] not in rotated_digits \
                    or rotated_digits[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
