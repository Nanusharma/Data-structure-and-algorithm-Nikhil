# https://leetcode.com/problems/k-divisible-elements-subarrays/?envType=problem-list-v2&envId=hash-table
from typing import List
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        def unique_subarrays(arr):
            n = len(arr)
            unique = set()  
            for i in range(n):
                for j in range(i + 1, n + 1):
                    subarray = tuple(arr[i:j]) 
                    unique.add(subarray)
            return list(unique)

        x = unique_subarrays(nums)
        print(x)
        count = 0 
        for arr in x:
            hash_map = {}
            for i in arr:
                if i in hash_map:
                    hash_map[i]+=1
                else:
                    hash_map[i]=1
            x = 0
            # print(hash_map)
            for i, itr in hash_map.items():
                # print(i, itr)
                if i%p == 0:
                    x+=itr
            if x <=k or x ==0:
                count+=1
        return count

obj = Solution()
nums = [1,2,3,4]
k = 4
p = 1
print(obj.countDistinct(nums,k,p))
            