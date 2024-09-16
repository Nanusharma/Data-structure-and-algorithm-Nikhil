class Solution():
    def duplicate(self, nums):
        hash_map = {}
        duplicate = []
        for i in nums:
            if i in hash_map:
                duplicate.append(i)
            else:
                hash_map[i] = 1
        return duplicate

obj = Solution()
nums = [1, 2, 3, 4,7,7,8,8,5,3]
print(obj.duplicate(nums))