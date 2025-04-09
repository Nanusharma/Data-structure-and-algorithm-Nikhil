# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=daily-question&envId=2025-03-19
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        oprx = -1
        count = 0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i] =1
                if nums[i+1] == 1:
                    nums[i+1] = 0
                else:
                    nums[i+1] =1
                if nums[i+2] == 1:
                    nums[i+2] = 0
                else:
                    nums[i+2] =1
                count+=1

        if nums[-1] and nums[-2] and nums[-3] == 1:
            oprx = count
            return count
        else:
            return oprx