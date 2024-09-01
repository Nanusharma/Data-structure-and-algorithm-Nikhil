# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/?envType=daily-question&envId=2024-08-03
from typing import List
class Solution():
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        # for i in range(len(arr)):
        #     if target[i] != arr[i]:
        #         return False
        # return True
        return target== arr
obj = Solution()
target= [1,2,3,4]
arr=[2,3,1,4]
print(obj.canBeEqual(target,arr))
