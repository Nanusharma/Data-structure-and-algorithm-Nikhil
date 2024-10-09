# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07
class Solution:
    def minLength(self, s: str) -> int:
        i = 0
        while i <len(s)-1:
            if s[i:i+2] == 'AB' or s[i:i+2] == 'CD':
                s = s[:i] + s[i+2:]
                i=0
            else:
                i+=1

        return len(s)
    
obj = Solution()
s = "ABFCACDB"
print(obj.minLength(s))


# optimal solution #

# class Solution:
#     def minLength(self, s: str) -> int:
#         while('AB' in s or 'CD' in s):
#             if 'AB' in s:
#                 s = s.replace('AB','')
            
#             if 'CD' in s:
#                 s = s.replace('CD','')
        
#         return len(s)