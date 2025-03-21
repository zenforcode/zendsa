from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        # Compute the left product for each index
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_produtpct *= nums[i]
            print(output)
        # Compute the right product and update the result
        print("*********")
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
            print(f"{i},nums[i]={nums[i]},{right_product},{output[i]}")
            print(output)
        
        return output
if __name__=="__main__":
    nums = [1,2,3,4]
    sol = Solution()
    outdata = sol.productExceptSelf(nums)
    print(outdata)
