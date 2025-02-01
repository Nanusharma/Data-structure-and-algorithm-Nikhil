# https://leetcode.com/problems/special-array-i/description/?envType=daily-question&envId=2025-02-01
from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = len(nums)
        if l==1:
            return True
        parity = True
        for i in range(1, l):
            if nums[i]%2 != nums[i-1]%2:
                pass
            else:
                return False
        return parity



        
        