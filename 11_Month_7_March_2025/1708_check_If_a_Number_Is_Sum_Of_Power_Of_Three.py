# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/?envType=daily-question&envId=2025-03-04

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while True:
            if n ==1 or n ==0:
                return True
            elif n == 2:
                return False
            x = int(n/3)
            if n-(x*3)== 2:
                return False
            elif n -(x*3)== 0 or n -(x*3)== 1:
                n = x