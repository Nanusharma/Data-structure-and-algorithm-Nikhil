# https://leetcode.com/problems/3sum/description/
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_subarray = []
        nums.sort()  
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    unique_subarray.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1  
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1 
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return unique_subarray