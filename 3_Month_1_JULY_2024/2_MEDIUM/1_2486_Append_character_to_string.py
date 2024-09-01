# LINK->TYPE->DATE
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/?envType=daily-question&envId=2024-06-03
# 2024-06-03 daily question
# MEDIUM
class Solution(object):
   def appendCharacters(self,s,t): 
      j=0
      count=0
      for i in range(len(s)):
        if j<len(t) and s[i]==t[j]:
            count+=1
            j+=1
      return len(t) - count    
         

sol=Solution()
s="coaching"
t="coding"
print(sol.appendCharacters(s,t))

