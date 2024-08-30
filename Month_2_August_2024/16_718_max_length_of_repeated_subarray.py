from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        subarray = [ ]
        for i in range(len(nums1)):
            j = len(nums1)
            while i < j:
                sub = nums1[i:j]
                subarray.append(sub)
                j-=1
        max_len = 0
        for i in range(len(nums2)):
            j = len(nums2)
            while i < j:
                if nums2[i:j] in subarray:
                    # print(f"nums2  {nums2[i:j]}")
                    max_len = max(max_len,len(nums2[i:j]))
                j-=1
        return max_len

obj = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
print(obj.findLength(nums1,nums2))