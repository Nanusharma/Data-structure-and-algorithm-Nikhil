# https://leetcode.com/problems/continuous-subarray-sum/?envType=daily-question&envId=2024-06-08
# 2024-06-08
# 
class Solution(object):   
    def checkSubarraySum(self, nums, k):
        count=0
        n=len(nums)
        for i in range(len(nums) - 1):
            print(nums[i])
            print(nums[i+1])
            print(sum)
            if (nums[i] + nums[i + 1]) % k == 0:
                count+=1
        return count>0
            

nums= [23,2,4,6,7]
k = 6
sol=Solution()
print(sol.checkSubarraySum(nums,k))