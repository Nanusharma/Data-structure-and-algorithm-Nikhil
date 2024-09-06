# https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05

from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (m + n)
        current_sum = sum(rolls)
        required_sum = total_sum- current_sum
        array = [i for i in range(1,7)]
        
        if required_sum < n or required_sum > 6*n:
            return []
        
        result= [1]*n

        remaining_sum = required_sum - n
        i = 0
        while remaining_sum > 0:
            increment = min(remaining_sum, 5)  # Increment by at most 5 to keep the roll <= 6
            result[i] += increment
            remaining_sum -= increment
            i += 1
        
        return result

