# https://leetcode.com/problems/kth-distinct-string-in-an-array/?envType=daily-question&envId=2024-08-05
from typing import List
# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         hash_map={}
#         for i in arr:
#             if i in hash_map:
#                 hash_map[i]+=1
#             else:
#                 hash_map[i]=1

#         distinct_strings = [key for key, value in hash_map.items() if value == 1]

#         if k <= len(distinct_strings):
#             return distinct_strings[k - 1]
#         else:
#             return ""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=""
        n=0
        print(d.items)
        for i in d:
            if d[i]==1:
                c=i
                n+=1
            if n==k:
                return i
        return ""
        # for i,j in d.items():
        #     if j==1:
        #         c=i
        #         n+=1
        #     if n==k:
        #         return i
        # return ""
obj = Solution()
arr = ["d","b","c","b","c","a"]
k = 2
print(obj.kthDistinct(arr,k))
