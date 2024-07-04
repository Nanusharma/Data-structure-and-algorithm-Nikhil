# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Medium

class Solution(object):
    def searchRange(self, nums, target):
        def first(nums,target):
            left,right=0,0
            while left<= right:
                mid=(left+right)//2
                if nums[mid]==target:
                    left=mid+1
        def last(nums,target):

        
        
        return first(nums,target), last(nums,target)
    
sol =Solution()

nums=[5,7,7,8,8,10]
target= 6
print(sol.searchRange(nums,target))   