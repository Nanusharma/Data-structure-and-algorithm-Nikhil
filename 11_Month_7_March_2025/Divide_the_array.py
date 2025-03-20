# https://leetcode.com/problems/divide-array-into-equal-pairs/?envType=daily-question&envId=2025-03-17
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_map = {}

        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1

        idx = True
        for i in hash_map:
            if hash_map[i]%2 != 0:
                idx = False
        return idx
 


            
            
        