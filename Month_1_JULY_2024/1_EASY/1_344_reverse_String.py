# https://leetcode.com/problems/reverse-string/description/?envType=daily-question&envId=2024-06-02/
# EASY
class Solution(object):
    def reverseString(self, s):
        j=1
        for i in range(len(s)//2):
            s[i], s[len(s)-j] =s[len(s)-j], s[i]
            j+=1
        return s

s=["h","e","l","l","o"]