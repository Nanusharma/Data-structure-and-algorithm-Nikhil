# https://leetcode.com/problems/word-subsets/?envType=daily-question&envId=2025-01-10
# 916_words_subsets
from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        matches = []
        hash_map = {}
        for i in words2:
            for j in i:
                if j in hash_map:
                    hash_map[j]+=1
                else:
                    hash_map[j]=1

        for i in words1:
            hash_map2= {}
            
            for j in i:
                if j in hash_map2:
                    hash_map2[j]+=1
                else:
                    hash_map2[j]=1

            print(hash_map)
            print(hash_map2)
            m = 0
            for k in hash_map:
                # print(k)
                if k in hash_map2 and hash_map2[k]>= hash_map[k]:

                    m+=1
                    print(m)
            # print(m)
            if m == len(hash_map):
                matches.append(i)

        return matches

obj = Solution()
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["eo","lo"]

# Output: ["google","leetcode"]
print(obj.wordSubsets(words1,words2))
        