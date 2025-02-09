# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,num in enumerate(numbers):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement]+1, i+1]

            hash_map[num]=i

obj = Solution()
numbers = [2,7,11,15]
target = 9
print(obj.twoSum(numbers, target))