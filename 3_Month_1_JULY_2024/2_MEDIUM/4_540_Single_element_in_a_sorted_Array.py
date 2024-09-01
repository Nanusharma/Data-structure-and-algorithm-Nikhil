# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Medium

# Time complexity =o(N)
# class Solution(object):
#     def singleNonDuplicate(self, nums):
#         hash_table={}
#         for i in nums:
#             if i in hash_table:
#                 hash_table+=1
#             else:
#                 hash_table[1]=1
        
#         for i in hash_table:
#             if hash_table[i]==1:
#                 return i


# Time complexity: O(log(n))

class Solution(object):
    def singleNonDuplicate(self, nums):
        left,right=0,len(nums)-1
        while left<right:
            mid= (left+right)//2
            is_even = (mid%2==0)
            if is_even:
                if nums[mid]==nums[mid+1]:
                    left=mid+2
                else:
                    right=mid
            else:
                if nums[mid]==nums[mid-1]:
                    left=mid+1
                else:
                    right =mid-1
        return nums[left]


   
sol= Solution()
# example:1
nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

print(sol.singleNonDuplicate(nums))
