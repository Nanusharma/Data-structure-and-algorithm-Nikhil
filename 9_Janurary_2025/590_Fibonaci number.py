# https://leetcode.com/problems/fibonacci-number/

class Solution:
    sum =0
    def fib(self, n: int) -> int:
        sum =0

        if n == 1:
            sum+=1

        elif n ==0:
            sum+=0
        
        if n>1:
            sum = self.fib(n-1)+self.fib(n-2)


        return sum
o = Solution()
n = 3

print(o.fib(n))
        
