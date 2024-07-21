# https://leetcode.com/problems/sort-colors/
# Inplace algortihm /can  only modify the nums 
# from typing import List
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         hash_table={}
#         for i in nums:
#             if i in hash_table:
#                 hash_table[i]+=1
#             else:
#                 hash_table[i]=1
#         num=[]
#         s=[0,1,2]
#         for i in s:
#             num.extend([i]*hash_table[i])
#         return num
        
        
# obj=Solution()
# nums = [2,0,2,1,1,0]
# print(obj.sortColors(nums))


from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_0=0
        count_1=0
        count_2=0
        for i in nums:
            if i ==0:
                count_0 +=1
            elif i==1:
                count_1+=1
            else:
                count_2+=1
        index = 0
        for _ in range(count_0):
            nums[index] = 0
            index += 1
        for _ in range(count_1):
            nums[index] = 1
            index += 1
        for _ in range(count_2):
            nums[index] = 2
            index += 1