# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        value_arr= []
        for i in s:
            value_arr.append(keyboard[i])
        print(value_arr)
obj =Solution()
s= "23"
print(obj.letterCombinations(s))

['abc', 'def']
# output =