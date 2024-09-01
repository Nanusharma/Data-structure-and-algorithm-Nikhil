# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

# we have to find the greatest common divisor of the both strings

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        hash_table={}
        for i in str1:
            if i in hash_table:
                hash_table[i]+=1
            else:
                hash_table=1
        print(hash_table)


sol=Solution()
str1 = "ABCABC"
str2 = "ABC"
# Output: "ABC"
# Example 2:

# str1 = "ABABAB"
# str2 = "ABAB"
# Output: "AB"

# str1 = "LEET"
# str2 = "CODE"
# Output: ""
print(sol.gcdOfStrings(str1,str2))
