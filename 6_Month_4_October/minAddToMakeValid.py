
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2024-10-09
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = ['A']
        for i in s:
            if i== ')' and stack[-1] == '(':
                stack.pop()

            else:
                stack.append(i)

            print(stack)

        return len(stack)-1


obj = Solution()
s = "()))(("
s = "(()))))"
print(obj.minAddToMakeValid(s))