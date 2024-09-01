# https://leetcode.com/contest/weekly-contest-407/problems/number-of-bit-changes-to-make-two-integers-equal/
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # conversion
        n_binary = bin(n)[2:]
        k_binary = bin(k)[2:]

        if len(k_binary) > len(n_binary):
            return -1

        max_len = max(len(n_binary), len(k_binary))
        n_binary = n_binary.zfill(max_len)
        k_binary = k_binary.zfill(max_len)

        for i in range(len(k_binary)):
            if k_binary[i] == '1' and n_binary[i] == '0':
                return -1

        
        change= 0
        for nbin, kbin in zip(n_binary, k_binary):
            if nbin == '1' and kbin == '0':
                change += 1

        return change

# Example usage
sol = Solution()
print(sol.minChanges(13, 4))  # Output: 2
print(sol.minChanges(21, 21))  # Output: 0
print(sol.minChanges(14, 13))  # Output: -1
