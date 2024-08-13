# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in matrix:
        #     for j in i:
        #         if j==target:
        #             return True
        #             break

        mid = len(matrix)%2
        while mid < len(matrix)-1:
            if matrix[mid][0]>target:
                mid-=1

            elif matrix[mid][len(matrix[0])-1] <  target:
                mid+=1
                # print(mid)
            elif target>matrix[mid][0] and target<matrix[mid][len(matrix[0])-1]:
                for i in matrix[mid]:
                    if i==target:
                        return True
                    
        # print([len(matrix[0])-1])




        
        # matrix[mid][0]< target and matrix[mid]
        



obj = Solution()
matrix = [[1,3,5,7],[10,13,16,20],[23,30,34,60]]
target = 13
print(obj.searchMatrix(matrix,target))