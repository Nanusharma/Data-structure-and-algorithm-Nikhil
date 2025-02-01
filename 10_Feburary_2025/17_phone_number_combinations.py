# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=backtracking

from typing import Lis
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = digits
        l = len(digits)
        combinations = []

        hash_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8": "tuv",
            "9" : "wxyz"
        }
        if l == 0:
            return []

        elif l == 1:
            return [i for i in hash_map[d]] # return list[hash_map[d]]
        
        elif l >1:
            arr = [hash_map[i] for i in d]   #arr = ["abc","def"]

            digits = ""
            def backtrack(index, current_combination):
                if index == len(arr):
                    combinations.append(current_combination)
                    return
                for i in arr[index]:
                    backtrack(index+1, current_combination+i)
            backtrack(0,"")

            return combinations
                


obj = Solution()
digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(obj.letterCombinations(digits))
