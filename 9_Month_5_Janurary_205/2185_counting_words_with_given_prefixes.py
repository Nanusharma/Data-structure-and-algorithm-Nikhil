# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/?envType=daily-question&envId=2025-01-09
from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        L = len(pref)
        count = 0
        for i in words:
            print(i[0:L])
            if len(i)>=L and i[0:L]== pref:
                count+=1
        return count
obj = Solution()
words = ["pay","attention","practice","attend"]
pref = "at"
print(obj.prefixCount(words,pref))
        