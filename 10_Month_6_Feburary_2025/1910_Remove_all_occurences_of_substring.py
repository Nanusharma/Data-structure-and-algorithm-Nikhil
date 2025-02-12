# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/?envType=daily-question&envId=2025-02-11


# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         stax = []
#         l_S = len(s)
#         l_P = len(part)
#         for i in range(l_S-l_P+1):
#             if s[i:i+l_P] == part:
#                 if i == 0:
#                     s = s[i+l_P:l_S]
#                 else:
#                     s = s[0:i-1] + s[i+l_P+1:l_S]
#             else:
#                 stax.append(s[i])
#             # print(s[i:i+l_P])
#         return s
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        
        for char in s:
            stack.append(char)
            if len(stack) >= len(part) and ''.join(stack[-len(part):]) == part:
                # Remove the part from stack if found
                for _ in range(len(part)):
                    stack.pop()
                    
        return ''.join(stack)
obj = Solution()

s = "daabcbaabcbc"
part = "abc"

# "dab"

s = "axxxxyyyyb"
part = "xy"

# "ab"

print(obj.removeOccurrences(s,part))