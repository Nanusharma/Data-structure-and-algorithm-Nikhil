# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1306052399/
# EASY
# /******TIME LIMIT EXCEEDED********/
# USE two pinter approach#

class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        a=len(nums)
        count=0
        while a>0:
            for i in range(len(nums)-1):
                if nums[i]==nums[i+1]:
                    for j in range(i,len(nums)-1):
                        nums[j],nums[j+1] = nums[j+1],nums[j]        
            a-=1
        hash_table={}
        for i in nums:
            if i in hash_table:
                break  # Stop counting if we encounter a previous element
            else:
                hash_table[i] = 1  # Add the element to the dictionary with initial count 1
                count += 1
        return count, nums
sol = Solution()
nums = nums = [1,1,2]
print(sol.removeDuplicates(nums))  # Output: [1, 2, 3]


