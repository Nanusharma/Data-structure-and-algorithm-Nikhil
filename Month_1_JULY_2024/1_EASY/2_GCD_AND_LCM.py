# https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

class Solution:
    def lcmAndGcd(self, A , B):
        a=A
        b=B
        GCD=1
        LCM=0
        while(A>0 and B>0):
            if A>B:
                A=A%B
            else:
                B=B%A
        if A==0:
            GCD= B
        if B==0:
            GCD=A
        
        LCM =(a * b) // GCD
       
        return LCM, GCD
            
sol = Solution()
A=5
B=10
print(sol.lcmAndGcd(A,B))