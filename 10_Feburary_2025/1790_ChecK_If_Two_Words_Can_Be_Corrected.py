# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/?envType=daily-question&envId=2025-02-05

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        hash_Map = {}
        hash_Map2= {}
        l = len(s1)
        for i in range(l):
            if s1[i] in hash_Map:
                hash_Map[s1[i]]+=1
            else:
                hash_Map[s1[i]] =1

            if s2[i] in hash_Map2:
                hash_Map2[s2[i]]+=1
            else:
                hash_Map2[s2[i]] =1

            if s1[i] != s2[i]:
                count+=1
        if (count == 0 or count == 2) and hash_Map == hash_Map2:
            return True
        else:
            return False

        