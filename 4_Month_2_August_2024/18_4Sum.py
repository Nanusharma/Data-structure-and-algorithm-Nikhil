# https://leetcode.com/problems/4sum/
from typing import List
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        array = []
        for i in range(len(nums)-4):
            for j in range(i,len(nums)-3):
                for k in range(j,len(nums)-2):
                    for l in range(k,len(nums)-1):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            array.append([i,j,k,l])

obj = Solution()
nums = [1,0,-1,0,-2,2] 
target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(obj.fourSum(nums,target))