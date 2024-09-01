from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start =0
        forward=0
        
# need first occurence


            
        start =0 
        while start <len(haystack):
            forward = 0
        while forward<len(needle) and start<len(haystack):
            print(forward)
            if haystack[start] != needle[forward]:
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
print(obj.strStr(haystack,needle))



from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        start = 0
        while start < len(haystack):
            forward = 0
            while forward < len(needle) and start + forward < len(haystack):
                if haystack[start + forward] != needle[forward]:
                    break
                forward += 1
            if forward == len(needle):
                return start
            start += 1
        
        return -1

obj = Solution()

haystack = "mississippi"
needle = "issip"
print(obj.strStr(haystack, needle))