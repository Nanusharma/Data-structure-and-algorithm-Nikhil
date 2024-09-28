# https://leetcode.com/problems/reverse-integer/
# We have to check the limits of x carefully
class Solution:
    def reverse(self, x: int) -> int:
      
        if x < -2**31 or x > 2**31 - 1:
            return 0

        if x < 0:
            number = -x
            re = str(number)[::-1] 
            re = int(re)
            re = -re  
        else:
            re = int(str(x)[::-1])  

        if re < -2**31 or re > 2**31 - 1:
            return 0
        
        return re

# x = 123
x = -123
obj = Solution()
print(obj.reverse(x))