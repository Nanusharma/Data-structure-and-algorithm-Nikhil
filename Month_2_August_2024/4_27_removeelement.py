from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        backward = len(nums) - 1
        
        while start <= backward:
            if nums[start] == val:
                nums[start], nums[backward] = nums[backward], nums[start]
                backward -= 1  
            else:
                start += 1
        
        return start