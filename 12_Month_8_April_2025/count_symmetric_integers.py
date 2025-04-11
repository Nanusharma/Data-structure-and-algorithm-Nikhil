# https://leetcode.com/problems/count-symmetric-integers/?envType=daily-question&envId=2025-04-11
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            if len(str(i))==4 or len(str(i))== 2:
                nums = [int(digit) for digit in str(i)]
                if len(nums) == 2:
                    if nums[0] == nums[1]:
                        count+=1
                else:
                    if nums[0]+nums[1] == nums[2]+nums[3]:
                        count+=1
        return count
                

