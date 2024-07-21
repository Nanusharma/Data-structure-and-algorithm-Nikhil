
class Solution:
    def findDuplicate(self, nums):
        hash_table={}
        for i in nums:
            if i in hash_table:
                hash_table[i]+=1
            else:
                hash_table[i]=1
        for i in hash_table:
            print(i)
            print(f"hash_table {hash_table[i]}")
            if hash_table[i]>1:
                return i
            print()

        # print(hash_table)
obj = Solution()
nums = [1,3,4,2,2]
obj.findDuplicate(nums)
        