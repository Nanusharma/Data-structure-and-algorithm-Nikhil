# https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=sliding-window
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash_map = {}
        for i in p:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1

        def hasht(s):
            hash_map = {}
            for i in a:
                if i in hash_map:
                    hash_map[i]+=1
                else:
                    hash_map[i]= 1
            return hash_map
            
        index = []
        left = 0
        right = len(p)

        while left<= len(s):
            print(left,right)
 
            a = s[left:right]
            # print(a)
            hash = hasht(a)
            if hash== hash_map:
                index.append(left)
                print(index)
                while s[right+1]== s[left]:
                    left+=1
                    right+=1
                    index.append(left)
                    print(index)

                if s[right+1] != s[left]:
                    left+=len(p)
                    right+=len(p)
                    print(f"up: {s[left:right]}")
            else:
                left+=len(p)
                right+=len(p)
                print(f"down: {s[left:right]}")


            # print(left,right)
            print(f"last: {s[left:right]}")
        return index


obj = Solution()
s = "cbaebabacd"
p = "abc"
print(obj.findAnagrams(s,p))