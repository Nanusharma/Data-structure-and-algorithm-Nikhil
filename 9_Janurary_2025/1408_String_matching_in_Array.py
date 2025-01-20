# https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07
from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches= []
        for i in words:
            L= len(i)
            for j in  words:
                print(i,j)
                if i in j and i != j:
                    matches.append(i)
                elif i == j:
                    continue
        return matches
                    



 


        
obj = Solution()
words = ["mass","as","hero","superhero"]
words= ["blue","green","bu"]
print(obj.stringMatching(words))