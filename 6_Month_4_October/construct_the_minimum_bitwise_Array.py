from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []  # Initialize the result array

        for n in nums:
            # Calculate the number of bits in n
            num_bits = n.bit_length()  # Number of bits required to represent n
            # Calculate the largest power of 2 that has the same number of bits
            lower_bound = (1 << (num_bits - 1))  # 2^(num_bits - 1)
            upper_bound = (1 << num_bits)  # 2^num_bits
            print(lower_bound, upper_bound)

            found = False
            
            # Check only within the valid range [lower_bound, upper_bound)
            for j in range(lower_bound, upper_bound):
                if (j | (j + 1)) == n:
                    ans.append(j)
                    found = True
                    break
            
            if not found:
                ans.append(-1)

        return ans
sol = Solution()
nums = [884532611, 741533369, 868936609, 816315823, 150570781, 346594697, 334726181, 921762641, 89355881, 403165729, 931242733]
result = sol.minBitwiseArray(nums)
print(result)
