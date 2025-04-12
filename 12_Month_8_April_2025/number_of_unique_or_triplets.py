# https://leetcode.com/contest/biweekly-contest-154/problems/number-of-unique-xor-triplets-i/
from typing import List
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique = set()
        n  = len(nums)
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    sub = sorted([nums[i], nums[j], nums[k]])

                    if sub[0]<= sub[1] <= sub[2]:
                        print(sub)
                        xor_value = nums[i] ^ nums[j] ^ nums[k]
                        unique.add(xor_value)
        return len(unique)


# class Solution:
#     def uniqueXorTriplets(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n ==1:
#             return 1 
#         elif n ==2:
#             return 2
#         return 1 << n.bit_length()


obj = Solution()
nums = [3,1,2,4] #it is not genertating [4,4,4] why?
print(obj.uniqueXorTriplets(nums))