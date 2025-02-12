# https://leetcode.com/problems/count-number-of-bad-pairs/?envType=daily-question&envId=2025-02-09
from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        l = len(nums)
        total_pairs = 0
        good_pairs = 0
        for i in range(l-1):

            for j in range(i+1, len(nums)):
                print(i,j)
                # print(j)
                if j - i == nums[j] - nums[i]:
                    good_pairs+=1
                total_pairs+=1

        return int((l * (l - 1)) / 2) - good_pairs
        n = l 
        print(int((n * (n-1)) / 2))

obj = Solution()
nums = [ 4,1,3,3]
print(obj.countBadPairs(nums))