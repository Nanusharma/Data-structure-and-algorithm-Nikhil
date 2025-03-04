# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        greater = []
        equals  = []
        for i in nums:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                equals.append(i)
                
        return smaller + equals + greater