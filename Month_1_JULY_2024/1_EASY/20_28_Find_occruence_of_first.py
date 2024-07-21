from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start =0
        forward=0
        
        while forward<len(needle) and start<len(haystack):
            print(forward)
            if haystack[start]!= needle[forward]:
                start+=1
                forward=0
            else:
                forward+=1
                start+=1
        print(forward)
        if forward>0:
            return start-forward
        else:
            return -1
        
obj =Solution()

haystack="mississippi"
needle="issip"
# haystack = "sadutsad"
# needle = "sad"
# haystack="leetcode"
# needle = "leeto"
print(obj.strStr(haystack,needle))
