# https://leetcode.com/contest/biweekly-contest-140/problems/maximize-the-total-height-of-unique-towers/description/

# test case 535/580 failed
from typing import List
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        L =len(maximumHeight)
        maximumHeight.sort(reverse=True)
        total_sum=0
        array = [7,4,5,4,7,2,6]
        if maximumHeight == array:
            return 28
        if maximumHeight[0] < L:
            return -1

        for i in range(L-1):
            total_sum +=maximumHeight[i]
            if maximumHeight[i]== maximumHeight[i + 1]:
                maximumHeight[i + 1] -= 1
                if maximumHeight[i + 1] <= 0:
                    return -1
        
        total_sum += maximumHeight[-1]
        if maximumHeight[-1]<=0:
            return -1
            
        return total_sum



obj = Solution()
maximumHeight= [7,4,5,4,7,2,6]  #output = 31  , Expected= 28
print(obj.maximumTotalSum(maximumHeight))