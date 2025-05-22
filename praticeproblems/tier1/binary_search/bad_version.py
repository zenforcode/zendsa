    
def isBadVersion(n: int) -> bool:
    pass 

def firstBadVersion(self, n: int) -> int:
    left, right = 1, n
    if n == 1 and isBadVersion(n):
        return n
    else:
         while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):
                right = mid -1
            elif not isBadVersion(mid):
                left = mid +1 
    return -1