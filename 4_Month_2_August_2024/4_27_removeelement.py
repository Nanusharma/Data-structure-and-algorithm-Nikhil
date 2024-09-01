# probem number 27 on leetcode
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        backward = len(nums) - 1
        
        while start <= backward:
            if nums[start] == val:
                nums[start], nums[backward] = nums[backward], nums[start]
                backward -= 1  
            else:
                start += 1
        
        return start
    

# from typing import List
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         start=0
#         backward=len(nums)-1
#         count=0
#         while start<=backward:
#             if nums[start]==val:
#                 if nums[start]!=nums[backward]:
#                     nums[start],nums[backward]= nums[backward],nums[start]
#                     # start+=1
#                     backward-=1

#                 else:
#                     backward-=1
#             else:
#                 start+=1
#         return start,nums
# obj =Solution()
# nums=[2]
# val=3
# print(obj.removeElement(nums,val))