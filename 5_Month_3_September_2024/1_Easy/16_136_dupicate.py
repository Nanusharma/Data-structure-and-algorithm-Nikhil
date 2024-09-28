# https://leetcode.com/problems/single-number/description/
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        duplicate = []
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1 
            else:
                hash_map[i] = 1
        for i in hash_map:
            if hash_map[i]==1:
                return i
            
nums = [1,1,2,2,3,3,5]
obj = Solution()
print(obj.singleNumber(nums)) 