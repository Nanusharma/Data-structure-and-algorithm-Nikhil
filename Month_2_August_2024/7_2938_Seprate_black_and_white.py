# https://leetcode.com/problems/separate-black-and-white-balls/
class Solution:
    def minimumSteps(self, s: str) -> int:
        i = 0
        j =len(s)-1
        min_steps=0
        print(s,s2)
        while i<=j:
            if s[i] =='1' and s[j]=='0':
                min_steps+=(j-i)
                i+=1
                j-=1
            elif s[i]=='1' and s[j]=='1':
                j-=1
            elif s[i]=='0' and s[j]=='1':
                i+=1
                j-=1
            else:
                i+=1
        return min_steps
obj = Solution()
s = "10010"
print(obj.minimumSteps(s))  # Output: 3