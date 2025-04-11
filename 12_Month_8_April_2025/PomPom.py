# https://leetcode.com/problems/subarray-product-less-than-k/?envType=problem-list-v2&envId=sliding-window

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        product = 1
        left = 0
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left+=1
            count+= right -left+1
        return count
        
obj = Solution()
nums = [10,2,5,6]
k = 100

print(f"pompom.py returns: {obj.numSubarrayProductLessThanK(nums,k)}")