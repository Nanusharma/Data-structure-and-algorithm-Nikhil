# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/?envType=daily-question&envId=2024-09-03
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        M = k
        hash_map = {chr(i): i - 96 for i in range(ord('a'), ord('z') + 1)}
        g= ""
        
        for i in s:
            digit = hash_map[i]
            g+=str(digit)
        
        k-=1
        sum=0
        print(g)
        for i in g:
            sum +=int(i)
        absolute_sum = 0   
        
        while k>0:
            sums = 0 
            for i in str(sum):
                sums+= int(i)
            sum = sums
            k-=1
            absolute_sum = sums
        
        if M ==1:
            return sum
        else:
            return absolute_sum

obj = Solution()
s = "qhquvppzooyt"
k = 6
obj.getLucky(s,k)

# By__Chatgpt

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Map each letter to its position in the alphabet
        hash_map = {chr(i): i - 96 for i in range(ord('a'), ord('z') + 1)}
        
        # Convert the string to its corresponding integer representation
        g = ''.join(str(hash_map[i]) for i in s)
        
        # First transform to get the initial sum
        sum_value = sum(int(digit) for digit in g)
        
        # Perform k-1 more transforms
        for _ in range(k - 1):
            sum_value = sum(int(digit) for digit in str(sum_value))
        
        return sum_value
        