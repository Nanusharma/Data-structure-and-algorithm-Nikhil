# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04

from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l = len(nums)-1
        i = 0
        maximum = 0 
        strictly_increasing = 0
        
        if l ==0:
            return nums[0]

        while i <= l:
            if i == l :
                if nums[i-1] < nums[i]:
                    strictly_increasing+=nums[i]
                    maximum = max(strictly_increasing, maximum)
                    i+=1
                else:
                    strictly_increasiing = nums[i]
                    maximum = max(strictly_increasing, maximum)
                    i+=1


            elif nums[i] < nums[i+1]:
                strictly_increasing +=nums[i]
                maximum = max(strictly_increasing, maximum)
                i+=1
            
            else:
                strictly_increasing += nums[i]
                maximum = max(maximum, strictly_increasing)
                print(maximum)
                strictly_increasing = 0
                i+=1

        return maximum



            

