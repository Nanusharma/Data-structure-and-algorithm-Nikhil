# # https://leetcode.com/problems/longest-common-prefix/


# Base code[1st iteration] [Complete code down below]
# from typing import List
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         n = 0
#         m = len(strs[0])
#         strs_len = len(strs)
#         str1 = ""
#         while n<=m:
#             count = 0
#             for i in range(len(strs)):
#                 word = strs[0][n]
#                 if strs[i][n]==word:
#                     count+=1
#                 else: 
#                     break
#             if count == strs_len:
#                 str1+=word
#             n+=1
#         return str1

# # strs = ["dog","racecar","car"]
# strs = ["flower","flow","flight"]
# obj = Solution()
# print(obj.longestCommonPrefix(strs))


# add exception handling if strs[i][n] index out of range return str1  [by chatgpt as i don't know how to use exception handling]

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = 0
        m = len(strs[0])
        strs_len = len(strs)
        str1 = ""
        
        while n <= m:
            count = 0
            try:
                word = strs[0][n]  
                for i in range(strs_len):
                    if strs[i][n] == word:
                        count += 1
                    else:
                        return str1
            except IndexError:
                return str1  
            if count == strs_len:
                str1 += word  
            else:
                return str1  
            n += 1  
        return str1

# Example usage:
# strs = ["flower", "flow", "flight"]
# strs = [ "pookie", "pookie","pookie"]
strs = ["dog","racecar","car"]
obj = Solution()
print(obj.longestCommonPrefix(strs))

# Can optimize it further.....