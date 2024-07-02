from typing import List

class Solution(object):
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 1
        i = 0
        total = 0
        for j in range(n):
            total += nums[j]
            while nums[j] * (j - i + 1) > total + k:
                total -= nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res

sol = Solution()
nums = [1, 2, 4]
k = 5
print(sol.maxFrequency(nums, k))  # Output: 3

nums = [1, 4, 8, 13]
k = 5
print(sol.maxFrequency(nums, k))  # Output: 2

nums = [3, 9, 6]
k = 2
print(sol.maxFrequency(nums, k))  # Output: 1