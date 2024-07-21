# https://leetcode.com/problems/two-sum/

from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map={}
#         for i in nums:
#             complement = target -i
#             if complement in hash_map:
#                 hash_map[complement]+=1
#             else:
#                 hash_map[complement]=1
#         for i in nums:
#             if target - i in hash_map:
#                 return i, hash_map[i]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i,num  in enumerate(nums):
            complement = target -num
            if complement in hash_map:
                return [hash_map[complement],i]
            hash_map[num]=i