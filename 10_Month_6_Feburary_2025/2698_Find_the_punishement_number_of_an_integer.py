# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/?envType=daily-question&envId=2025-02-15

class Solution:
    def check_digit_combinations(self, num):
        square = num * num
        str_square = str(square)
        
        def check_partition(parts):
            return sum(int(p) for p in parts) == num
        
        def generate_partitions(s, idx=0, current=[]):
            if idx == len(s):
                return check_partition(current)
            
            for i in range(idx + 1, len(s) + 1):
                if generate_partitions(s, i, current + [s[idx:i]]):
                    return True
            
            return False
        
        return generate_partitions(str_square)

    def punishmentNumber(self, n):
        return sum(i * i for i in range(1, n + 1) if self.check_digit_combinations(i))


obj = Solution()
n = 100
print(obj.punishmentNumber(36))
