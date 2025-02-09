# https://leetcode.com/problems/number-of-ways-to-split-array/?envType=daily-question&envId=2025-01-03

from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        L = len(nums)
        sum=0
        count=0
        for i in range(L):
            sum+=nums[i]
            nums[i]= sum
        for i in range(L-1):
            if nums[i]>= (nums[L-1]- nums[i]):
                count+=1
        return count

obj = Solution()
# nums = [1,2,3,0,3,2,0,-1]
nums =[2,3,1,0]
# nums = [10,4,-8,7]
print(obj.waysToSplitArray(nums))


        
        