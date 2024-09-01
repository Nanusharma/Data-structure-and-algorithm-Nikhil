# https://leetcode.com/problems/score-of-a-string/?envType=daily-question&envId=2024-06-01
# EASY

class Solution(object):
    def scoreOfString(self, s):
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
    
sol =Solution()
s="hello"
sol.scoreOfString(s)