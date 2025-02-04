from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0,0 
        m = len(nums1)
        n = len(nums2)
        curr = 0
        prev = 0
        if (m + n) %2 != 0:
            mn = (m+n)//2
            print(mn)
            while (i+j) <= mn:
                if nums1[i] < nums2[j]:
                    curr = nums1[i]
                    i+=1
                elif nums1[i]> nums2[j]:
                    curr = nums2[j]
                    j+=1
                elif nums1[i]==nums2[j]:
                    if i<=m-1:
                        curr = nums1[i]
                        i+=1
                    else:
                        curr = nums2[j]    
                        j+=1
            return curr
        else:
            mn = (m+n)//2
            while (i+j) <= mn:
                print(f"i,j{i,j}")
                if nums1[i] < nums2[j]:
                    if i < m:
                        prev = curr
                        curr = nums1[i]
                        print(f"Second: {prev,curr}")
                        i+=1
                    else:
                        prev = curr
                        curr = nums2[j]
                        j+=1
                        print(f"first: {prev,curr}")
                                                
                elif nums1[i]> nums2[j]:
                    prev = curr
                    curr = nums2[j]
                    j+=1;
                elif nums1[i]==nums2[j]:
                    if i<=m-1:
                        prev = curr
                        curr = nums1[i]
                        i+=1
                    else:
                        prev = curr
                        curr = nums2[j]    
                        j+=1
            print(prev, curr)
            return (prev+curr)//2

        
obj = Solution()
nums1 = [1,2]
nums2 = [3,4]
# nums1 = [1,5]
# nums2 = [6,6,7]

print(obj.findMedianSortedArrays(nums1,nums2))