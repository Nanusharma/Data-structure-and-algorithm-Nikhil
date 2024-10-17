# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/?envType=daily-question&envId=2024-10-11
from typing import List
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = sorted(times)
        print(times)
        
obj = Solution()
times = [[3,10],[1,5],[2,6]]
targetFriend = 0
print(obj.smallestChair(times, targetFriend))