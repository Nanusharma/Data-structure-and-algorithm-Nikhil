# https://leetcode.com/problems/lemonade-change/?envType=daily-question&envId=2024-08-15
''' solvable using if else statements, i use dictionary withouyt any reason
chatgpt solution below
'''
# from typing import List
# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         hash_map = {5:0,10:0,20:0}
#         for i in bills:
#             if i == 5:
#                 hash_map[5]+=1
#             if i ==10:
#                 if hash_map[5]>=1:
#                     hash_map[5]-=1
#                     hash_map[10]+=1
#                 else:
#                     return False
#             if i ==20:
#                 hash_map[20]+=1
#                 if hash_map[10]>=1 and hash_map[5]>=1:
#                     hash_map[10]-=1
#                     hash_map[5]-=1
#                 elif hash_map[5]>=3:
#                     hash_map[5]-=3
#                 else:
#                     return False
#         return True
# obj = Solution()
# # bills = [ 5,5,5,20,10]
# bills = [ 5,5,5,10,20]
# print(obj.lemonadeChange(bills))

# chatgpt
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count = 0  # To keep track of the number of $5 bills
        ten_count = 0   # To keep track of the number of $10 bills

        for bill in bills:
            if bill == 5:
                five_count += 1  # No change needed, just collect the $5 bill
            elif bill == 10:
                if five_count >= 1:
                    five_count -= 1  # Give one $5 bill as change
                    ten_count += 1   # Collect the $10 bill
                else:
                    return False  # Cannot provide correct change
            elif bill == 20:
                if ten_count >= 1 and five_count >= 1:
                    ten_count -= 1  # Give one $10 bill as part of change
                    five_count -= 1  # Give one $5 bill as part of change
                elif five_count >= 3:
                    five_count -= 3  # Give three $5 bills as change
                else:
                    return False  # Cannot provide correct change
        
        return True