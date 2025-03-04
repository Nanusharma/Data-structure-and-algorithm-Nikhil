# https://leetcode.com/problems/rearrange-array-elements-by-sign/
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        lPos = int(len(nums)/2)
        merged = [0]*(2*lPos)
        for i in range(lPos):
            merged[2 * i] = pos[i] 
            merged[2 * i + 1] = neg[i]

        return merged

