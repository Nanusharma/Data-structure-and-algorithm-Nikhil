# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/?envType=daily-question&envId=2025-01-04

# class Solution():
#     def countPallindromicSubsequence(self,s:str)-> int:
#         L = len(s)
#         count = 0
#         for i in range(L-2):
#             j = i+2
#             while j <= L-1:
#                 if s[i]==s[j]:
#                     print(f"{s[i], i}, {s[j], j}")
#                     count+=1
#                     j+=1
#                 else:
#                     j+=1
#         return count
# obj = Solution()
# s= "bbcbaba"
# print(obj.countPallindromicSubsequence(s))




class Solution():
    def countPallindromicSubsequence(self,s:str)-> int:
        count= 0 
        L =len(s)-1  # len = 7, len(s)-1 = 6 [1,2,3,4,5,]
        hash_map = {}
        for i in range(L-1): # till 5 [0,1,2,3,4,5]
            if s[i] not in hash_map:
                print(s[i])
                hash_map[s[i]]= True
                unique_chars = []
                
                for j in range(L,i+1,-1):  # .[6,5,4,3,2]
                    if s[i] == s[j]:
                        # print(f"{s[i], s[j]}")
                        for k in range(i+1,j):
                            if s[k] not in unique_chars:
                                unique_chars.append(s[k])
                                count+=1
                                print(f"{s[i],s[k],s[j]}")
                        break
        return count


obj = Solution()
# s= "bbcbaba"
s =  "aabca"
print(obj.countPallindromicSubsequence(s))
 