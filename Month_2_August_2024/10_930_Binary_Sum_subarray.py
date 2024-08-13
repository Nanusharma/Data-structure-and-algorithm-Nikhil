# https://leetcode.com/problems/binary-subarrays-with-sum/?envType=daily-question&envId=2024-08-10
from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         subarray = nums[i:j+1]
        #         if sum(subarray)==goal:
        #             count+=1
                       
        # return count

        i = 0
        j=1
        while i<len(nums):
            sub = nums[i:j]
            print(sub)
            if sum(sub)==goal:
                count+=1
            
            if j == len(nums):
                i+=1
                j=i
            j+=1
        return count
# Solution is right but, Time Limit exceeded
obj = Solution()
nums = nums = [1,0,1,0,1]
goal = 2
print(obj.numSubarraysWithSum(nums,goal))

# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]how to
# arr = [1,0,1]
# # if arr.sum== 2:
# #     print("True")
# j=0
# if sum(arr)== 2:
#     print("hefie")
# for i in arr:
#     j+=i
# print(j)