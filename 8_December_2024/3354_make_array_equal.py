from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        l = len(nums)
        zero_Array = []
        # Collect indices of zero elements
        for i in range(l):
            if nums[i] == 0:
                zero_Array.append(i)
        # Define array_Element function
        def array_Element(value):
            valid_Counts = 0
            # dir = value  # Can be 'R' or 'L'
            for i in zero_Array:
                curr = i
                dup_Arr = nums[:]
                dir = value
                while 0<=curr<l:  
                    if dup_Arr[curr] == 0 and dir == "R":
                        curr += 1
                    elif dup_Arr[curr] > 0 and dir == "R":
                        dup_Arr[curr] -= 1
                        dir = "L"
                        curr-=1
                    elif dup_Arr[curr] == 0 and dir == "L":
                        curr -= 1
                    elif dup_Arr[curr] > 0 and dir == "L":
                        dup_Arr[curr] -= 1
                        dir = "R"
                        curr += 1

                # Check if all elements in dup_Arr are zero
                if all(val == 0 for val in dup_Arr):
                    valid_Counts += 1
            return valid_Counts
        # Calculate results for "R" and "L"
        x = array_Element("R")
        y = array_Element("L")
        return x + y
nums = [16,13,10,0,0,0,10,6,7,8,7]
obj = Solution()
print(obj.countValidSelections(nums))