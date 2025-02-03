# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2025-02-03
from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        strictly_increasing =1
        strictly_decreasing = 1
        maximum = 0
        if len(nums) ==1:
            return 1 
        for i in range(len(nums)-1):
            if nums[i+1] > nums [i]:
                strictly_increasing+=1
                strictly_decreasing = 1
                maximum =  max(maximum,strictly_increasing,strictly_decreasing)
                
            elif nums[i+1] < nums[i]:
                strictly_decreasing += 1
                strictly_increasing = 1
                maximum =  max(maximum,strictly_increasing,strictly_decreasing)

            elif nums[i+1] == nums[i]:
                strictly_increasing = 1
                strictly_decreasing =1 
                maximum =  max(maximum,strictly_increasing,strictly_decreasing)
        
        return maximum