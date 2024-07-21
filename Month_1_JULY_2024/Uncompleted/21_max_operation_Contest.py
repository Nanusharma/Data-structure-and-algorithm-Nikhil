# leetcode.com/contest/weekly-contest-407/problems/maximum-number-of-operations-to-move-ones-to-the-end/
class Solution:
    def maxOperations(self, s: str) -> int:
        s = list(s)
        non_zero_index=0
        count=0
        for i in range(len(s)):
            if s[i] != '0':
                s[non_zero_index] = s[i-1]
                non_zero_index += 1
                count+=1
                print(s)
        return count
obj=Solution()
s = "00111"
print(obj.maxOperations(s))
