# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/?envType=daily-question&envId=2024-08-05
from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        num_len =len(set(nums))
        count=0
        for i in nums:
            if i >=num_len:
                count+=1
        if count==0:
            return-1
        else:
            return count
            
        # return -1
obj = Solution()
nums = [0,4,3,0,4]
nums= [0,0]
print(obj.specialArray(nums))
            