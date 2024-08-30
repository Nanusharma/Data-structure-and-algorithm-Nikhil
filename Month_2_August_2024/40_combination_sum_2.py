# https://leetcode.com/problems/combination-sum-ii/?envType=daily-question&envId=2024-08-13
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        targeted_equivalent_subarrays = []
        candidates.sort()

        for i in range(len(candidates)):
            if candidates[i] > target:
                candidates = candidates[:i]
                break

        i = 0
        j = 0 
        # 1,1,2,5,6,7
        while i < len(candidates): 
            if i < j:
                subarray = candidates[i:j]
                print(subarray)
                subarray_sum = sum(subarray)

                if subarray_sum == target:
                    targeted_equivalent_subarrays.append(subarray)
                elif subarray_sum > target:
                    i += 1
                    j = i
                    continue

            if j < len(candidates):
                j += 1
            else:
                i += 1
                j = i + 1
                
        return sorted(targeted_equivalent_subarrays)
obj = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(obj.combinationSum2(candidates,target))