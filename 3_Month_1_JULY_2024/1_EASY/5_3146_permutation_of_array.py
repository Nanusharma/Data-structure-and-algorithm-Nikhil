# https://leetcode.com/problems/permutation-difference-between-two-strings/description/
# EASY

class Solution(object):
    def findPermutationDifference(self, s, t):
        hash_table={}
        n=len(s)
        count=0
        index=0
        for i in range(n):
            if t[i] not in hash_table:
                hash_table[t[i]]=index
                index+=1
        for i in range(n):
            count+=abs(hash_table[s[i]]-i)
        return count
# {'b': 0, 'a': 1, 'c': 2}
sol=Solution()
s="abc"
t="bac"
print(sol.findPermutationDifference(s,t))
        