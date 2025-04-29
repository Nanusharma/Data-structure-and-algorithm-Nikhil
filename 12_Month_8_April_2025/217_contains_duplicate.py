from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return True if len(nums)-len(set(nums)) != 0 else False
        hash_map = {}
        for i in nums:
            if i in nums:
                return True
            else:
                hash_map[i]=1
        return False

obj = Solution()
nums = [1,2,3,4]
print(obj.containsDuplicate(nums))