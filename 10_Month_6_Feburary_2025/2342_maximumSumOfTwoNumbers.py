from typing import List
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxSum = -1
        hashMap = {}
        hashMap2 = defaultdict(list)

        for i in nums:
            num = i 
            sumDigits = 0
            while num > 0:
                sumDigits += num % 10  # Extract the last digit
                num //= 10 
            if sumDigits in hashMap or sumDigits in hashMap2:
                if sumDigits in hashMap2:
                    hashMap2[sumDigits].append(i)

                else:
                    hashMap2[sumDigits].append(hashMap[sumDigits])
                    hashMap2[sumDigits].append(i)
                    del hashMap[sumDigits]
            else:
                hashMap[sumDigits] = i 

        for key, values in hashMap2.items():
            if len(values)> 1:
                values.sort(reverse=True)  # Sort in descending order
                maxSum = max(maxSum, values[0] + values[1])  # Take top 2 values
        return maxSum
            

            # else:
            #     hashMap[sumDigits] = i 
        
        print(hashMap2)
# nums = [18,43,36,13,7]   // 9  7  9  4   7 


# 267 ms, 89.80
obj = Solution()
nums = [18,43,36,13,7]
print(obj.maximumSum(nums))