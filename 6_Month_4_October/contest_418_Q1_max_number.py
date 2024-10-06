from typing import List
import itertools

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        binary_map = {i: bin(i).replace("0b", "") for i in nums}
        
        max_number = 0

        for perm in itertools.permutations(nums):
           
            binary_str = ''.join([binary_map[i] for i in perm])
            
            decimal_number = int(binary_str, 2)
            max_number = max(max_number, decimal_number)
        return max_number

obj = Solution()
nums = [8, 2, 16]
print(obj.maxGoodNumber(nums))
