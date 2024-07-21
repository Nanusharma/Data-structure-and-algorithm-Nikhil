from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] ==0:
                nums.append(nums[i])
                nums.remove(nums[i])
        return nums
obj = Solution()
nums= [0,1,0,3,12]
print(obj.moveZeroes(nums))
        

# GPT
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer to track the position of the next non-zero element
        last_non_zero_found_at = 0
        
        # Move all non-zero elements to the beginning of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1
        
        # Fill the remaining positions with zeros
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0

# Example usage
obj = Solution()
nums = [0, 1, 0, 3, 12]
obj.moveZeroes(nums)
print(nums)  # Output should be [1, 3, 12, 0, 0]
