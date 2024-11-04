from typing import List
class Solution():
    def maximumSwap(self,num:int )->int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for larger in range(9, int(d), -1):
                if larger in last and last[larger] >i:
                    digits[i],digits[last[larger]] =digits[last[larger]], digits[i]
                    return int(''.join(digits))
        return num
obj = Solution()
num = 2736
print(obj.maximumSwap(num))

