from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums)== 3:
            return  max(nums[0], nums[1],nums[2])


        elif len(nums) % 2 == 0 and len(nums)>2:
            even_count = 0
            odd_count = 0
            for i in range(len(nums)):
                if i % 2 == 0:
                    odd_count += nums[i]
                else:
                    even_count += nums[i]
            return max(even_count, odd_count)


        else:
            count1 = 0  
            count2 = 0 
            count3 = 0  

            
            for i in range(1, len(nums), 2):
                count1 += nums[i]
    
            for i in range(len(nums) - 1):
                if i % 2 == 0:
                    count2 += nums[i]

            for i in range(1, len(nums)):
                if i % 2 == 0:
                    count3 += nums[i]

            return max(count1, count2, count3)


obj = Solution()
# nums= [0,1,2,3,4,5,6]
# nums= [1,2,3,1,4]
nums = [2,3,2,3,4,235,3,5,235,23,5,23,5,46,6,7,7]

print(obj.rob(nums))  # Output: 4