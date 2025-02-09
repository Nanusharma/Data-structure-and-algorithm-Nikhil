# https://leetcode.com/problems/count-vowel-strings-in-ranges/?envType=daily-question&envId=2025-01-02
from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []*len(queries)
        prefix_Sum = []*len(words)
        count = 0
        vowels = {'a','e','i','o','u'}
        for i in words:
            if i[0] in vowels and i[-1] in vowels:
                count += 1 
            prefix_Sum.append(count) 

        # print(prefix_Sum) [1, 1, 2, 3, 4] 
        for i in queries:
            l, r = i
            if l==0:
                ans.append(prefix_Sum[r])
            else:
                ans.append(prefix_Sum[r]-prefix_Sum[l-1])
        return ans

obj= Solution()
words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

print(obj.vowelStrings(words,queries))