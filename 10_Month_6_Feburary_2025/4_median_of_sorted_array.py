from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0,0 
        m = len(nums1)
        n = len(nums2)
        arr= []
        mn = (m+n)//2
        while (i+j) <= mn:
            if i == m or j == n:
                if i == m:
                    arr.append(nums2[j])
                    j+=1
                elif j == n:
                    arr.append(nums1[i])
                    i+=1
            elif nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i+=1
            elif nums1[i]> nums2[j]:
                arr.append(nums2[j])
                j+=1
            elif nums1[i]==nums2[j]:
                if i<=m-1:
                    arr.append(nums1[i])
                    i+=1
                else:
                    arr.append(nums2[j])
                    j+=1
        if (m + n) %2 != 0:
            return arr[-1]
        else:
            return (arr[-2]+arr[-1])/2


obj = Solution()
nums1 = [2]
nums2 = []
nums1 = [1,5]
nums2 = [6,6,]
print(obj.findMedianSortedArrays(nums1,nums2))