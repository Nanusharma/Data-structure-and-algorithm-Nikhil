# Leetcode problem number: 11
# solution after using the hints from the description of the question
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        forward = 0
        backward = len(height)-1
        while forward < backward:
                area = ((backward - forward)) * min(height[forward], height[backward])
                max_area = max(max_area, area)
                if height[forward]>height[backward]:
                      backward -= 1
                else:
                      forward+=1

        return max_area
    
obj = Solution()
height = [1,8,100,2,100,4,8,3,7]
print(obj.maxArea(height))  


# Soluton before reading the Hints from the description of the Question
#  from typing import List
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#         forward = 0
#         backward = len(height)-1
#         while forward < backward:
#             for i in range(forward,backward):
#                 area = ((backward - i)) * min(height[i], height[backward])
#                 max_area = max(max_area, area)
#             if height[forward]>height[backward]:
#                 backward -= 1
#             else:
#                 backward-=1

#         return max_area
    
# obj = Solution()
# height = [1,8,100,2,100,4,8,3,7]
# print(obj.maxArea(height))  

