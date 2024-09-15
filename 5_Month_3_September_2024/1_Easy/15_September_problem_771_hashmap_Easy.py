# Problem number 771 Easy Company tags: META
# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_table = []
        for i in stones:
            if i in hash_table:
                hash_table[i]+=1
            else:
                hash_table=1
        count=0
        for i in jewels:
            if i in hash_table:
                count+=hash_table[i]
        return count

#  Top Solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        aux = set(jewels)
        return sum((1 for x in stones if x in aux))