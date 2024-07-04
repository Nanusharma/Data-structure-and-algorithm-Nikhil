# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/?envType=daily-question&envId=2024-07-03
# MEDIUM


# ############----CHATGPT-SOLUTION------############

class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If there are less than or equal to 4 elements, we can make all elements the same in at most 3 moves.
        if len(nums) <= 4:
            return 0

        # Sort the array
        nums.sort()
        
        # Compute the minimum difference for the 4 possible scenarios
        min_diff = float('inf')
        
        # Scenario 1: Change the three largest elements
        min_diff = min(min_diff, nums[-4] - nums[0])
        
        # Scenario 2: Change the two largest and the smallest element
        min_diff = min(min_diff, nums[-3] - nums[1])
        
        # Scenario 3: Change the largest and the two smallest elements
        min_diff = min(min_diff, nums[-2] - nums[2])
        
        # Scenario 4: Change the three smallest elements
        min_diff = min(min_diff, nums[-1] - nums[3])
        
        return min_diff

# Example usage:
solution = Solution()
print(solution.minDifference([5, 3, 2, 4]))        # Output: 0
print(solution.minDifference([1, 5, 0, 10, 14]))  # Output: 1
print(solution.minDifference([3, 100, 20]))       # Output: 0
