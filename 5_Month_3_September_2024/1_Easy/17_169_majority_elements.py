# https://leetcode.com/problems/majority-element/
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0 
        for num in nums:
            if count == 0:
                candidate = num
                count+=1
            elif candidate == num:
                count += 1
            else:
                count-=1
        return candidate

obj= Solution()
nums = [2,2,1,1,1,2,2]
print(obj.majorityElement(nums))