# https://leetcode.com/problems/permutation-in-string/description/?envType=daily-question&envId=2024-10-05
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        L = len(s2)

        hash_map = {}
        for k in s1:
            if k in hash_map:
                hash_map[k]+=1
            else:
                hash_map[k]=1
        while i <= L-j:
            s = s2[i:i+j]
            hash_map2={}
            for o in s:
                if o in hash_map2:
                    hash_map2[o]+=1
                else:
                    hash_map2[o]=1
            if hash_map == hash_map2:
                return True
            i+=1
        
        return False


obj = Solution()
# s1 = "ab"
# s2= "eidbaooo"
s1= "ab"
s2 = "eidboaoo"

print(obj.checkInclusion(s1,s2))

# Time taken 28 minutes
# 5 october 2024 18:01 pm 