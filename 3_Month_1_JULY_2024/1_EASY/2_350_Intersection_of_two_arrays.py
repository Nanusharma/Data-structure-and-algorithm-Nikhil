# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2024-07-02
# EASY
class Solution(object):
    def intersect(self, nums1, nums2):
        intersect=[]
        if len(nums1)<len(nums2):
            max=nums2
            min=nums1
        else:
             max = nums1
             min = nums2

        hash_table={}
        for i in max:
            if i in hash_table:
                hash_table[i]+=1
            else:
                hash_table[i]=1

        for i in min:
            if i in hash_table and hash_table[i]>0:
                intersect.append(i)
                hash_table[i]-=1
        return intersect
sol= Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# Output: [4,9]

print(sol.intersect(nums1, nums2))

#LEETCODE SOLUTION

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res = []
        
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
                
        return res

