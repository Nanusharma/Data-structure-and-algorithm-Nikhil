# https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-09-03
from typing import List
class Solution:
    def __init__(self) -> None: #automatic execution at the time of the decleration of the object 
        print("who's gonna stop me from execution")
        print("i am gonna execute at the time of decleration of an object")


    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        if k ==1:
            return max(happiness)
        else:
            happiness.sort()
            Last = len(happiness)-1
            N = 0
            sums = 0 
            while k >=1:
                if happiness[Last-N]-N <0:
                    sums+=0
                else:
                    sums+=happiness[Last-N]-N
                N+=1
                k-=1
	        
            return sums
obj = Solution() #decleration of the object
happiness= [12,1,42]
k =3
obj.maximumHappinessSum(happiness,k) # what is this called ass???
# print(obj.maximumHappinessSum(happiness,k))