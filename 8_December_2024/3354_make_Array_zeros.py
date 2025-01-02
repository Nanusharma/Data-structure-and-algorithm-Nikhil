from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        l = len(nums)
        zero_Array = []
        # Collect indices of zero elements
        for i in range(l):
            if nums[i] == 0:
                zero_Array.append(i)
                
        def array_Element(value):
            valid_Counts = 0
            for i in zero_Array:
                curr = i
                dir = value  # Can be 'R' or 'L'
                dup_Arr = nums[:]
                
                while 0 <= curr < l:
                    if dup_Arr[curr] == 0 and dir == "R":
                        curr += 1
                    elif dup_Arr[curr] == 0 and dir == "L":
                        curr -= 1
                    elif dup_Arr[curr] > 0 and dir == "R":
                        dup_Arr[curr] -= 1
                        dir = "L"
                        curr -= 1
                    elif dup_Arr[curr] > 0 and dir == "L":
                        dup_Arr[curr] -= 1
                        dir = "R"
                        curr += 1
                        
                if all(val == 0 for val in dup_Arr):
                    valid_Counts += 1
            return valid_Counts
            
        return array_Element("R") + array_Element("L")