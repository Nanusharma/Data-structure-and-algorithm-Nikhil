from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # NotDuplicate=[]
        # start= 0
        # forward=0
        # count=0
        # while start<=len(nums):
        #     count+=1
        #     print(f"Count{count}")
        #     if nums[start]==nums[forward]:
        #         forward+=1
        #     else:
        #         NotDuplicate.append(nums[start])
        #         forward+=1
        #         start=forward
        #     print(f"forward{forward}")
        # for i in NotDuplicate:
        #     nums[i]=NotDuplicate[i]
        # print(nums)
        # return len(NotDuplicate)
    #     class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # i = 0
        
        # for j in range(1, len(nums)):
        #     if nums[j] != nums[i]:
        #         i += 1
        #         nums[i] = nums[j]
        # return i + 1

        hash_map ={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        print(hash_map)

        for i,j in enumerate(hash_map):
            nums[i]=j
        
        # for i, j in enumerate(hash_map):
        #     nums[i]

        #     print(i)
            # print(hash_map[i])
obj =Solution()
nums=  [0,2,2,3,3,4]
print(obj.removeDuplicates(nums))




# chatg[t

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the slow pointer
        i = 0
        
        # Use the fast pointer to iterate through the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # Return the number of unique elements, which is i + 1
        return i + 1