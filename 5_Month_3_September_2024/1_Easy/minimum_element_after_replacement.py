# https://leetcode.com/contest/biweekly-contest-140/problems/minimum-element-after-replacement-with-digit-sum/description/
from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:
        minimum = nums[0]
        for num in nums:
            sum_num = sum(int(digit) for digit in str(num))
            minimum = min(minimum, sum_num)
        return minimum


obj = Solution()
nums = [10,12,13,14]
print(obj.minElement(nums))
