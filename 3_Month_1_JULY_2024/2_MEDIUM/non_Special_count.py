# https://leetcode.com/contest/weekly-contest-408/problems/find-the-count-of-numbers-which-are-not-special/
import math
import time
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # fprime genrator
        def generate_primes(n):
            prime = [True] * (n + 1)
            prime[0], prime[1] = False, False
            for i in range(2, int(n**0.5) + 1):
                if prime[i]:
                    for j in range(i * i, n + 1, i):
                        prime[j] = False
            return [x for x in range(2, n + 1) if prime[x]]
        
        max_sqrt = int(math.sqrt(r)) + 1 #math sqrt
        prime_number = generate_primes(max_sqrt)
        print(prime_number)
        
        special_number = 0
        for prime in prime_number:
            prime_square = prime * prime
            if l <= prime_square <= r:
                special_number += 1
        
        total_numbers = r - l + 1 #range  +1
        
        return total_numbers - special_number
obj = Solution()
l=364
r= 21316
# 20927
start_time = time.time()
result = obj.nonSpecialCount(l, r)
end_time = time.time()
# print(f"Result: {result}")
print(f"Execution time: {end_time - start_time} seconds")


# from typing import List
# import time
# class Solution:
#     # class Solution:
    
#     def nonSpecialCount(self, l: int, r: int) -> int:
#         count_1=0
#         for i in range(l,r+1):
#             count=0
#             for j in range(1,i):
#                 if i%j==0:
#                     count+=1
#                     if count==2:
#                         break
#             if count==2:
#                 count_1+=1
#         return (r+1)-l-count_1        

# obj = Solution()
# l=364
# r= 21316
# # 20927
# start_time = time.time()
# result = obj.nonSpecialCount(l, r)
# end_time = time.time()
# print(f"Result: {result}")
# print(f"Execution time: {end_time - start_time} seconds")