# https://leetcode.com/problems/search-insert-position/


##############----O(n)_time-----######
# class Solution(object):
#     def searchInsert(self, nums, target):
#         for i in range(len(nums)):
#             if nums[i] == target or nums[i]> target:
#                 return i 
#         else:
#             return len(nums)
        


##############----O(log(n))_time-----######
class Solution(object):
    def searchInsert(self, nums, target):
        left,right=0,(len(nums))-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target or nums[mid]> target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return len(nums)
        
sol= Solution()
nums=[1,3,5,6]
target = 2
print(sol.searchInsert(nums,target))