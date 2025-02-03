class Solution:
    def findValidPair(self, s: str) -> str:
        hash_map = {}
        for i in s:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1

        if len(hash_map)==1:
            return ""

        s = ""
        for i in hash_map:
            if int(i) == hash_map[i]:
                s = s+i
        return s


                
#         print(len(hash_map))

obj = Solution()
s = "2523533"
print(obj.findValidPair(s))