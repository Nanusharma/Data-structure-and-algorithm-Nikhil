##############----O(n)_time-----######

# class Solution(object):
#     def search(self, nums, target):
#         for i in range(len(nums)):
#             if nums[i]==target:
#                 return i 
#         else:
#             return -1


#########----o(log(n))_time----#########
class Solution(object):
    def search(self, nums, target):
        left,right=0,len(nums)-1
        while left <=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1


sol= Solution()
nums=[-1,0,3,5,9,12]
target = 2
print(sol.search(nums,target))