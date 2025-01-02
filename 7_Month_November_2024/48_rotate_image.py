# # https://leetcode.com/problems/rotate-image/description/
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                # Swap elements
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

    

        return matrix
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = 0 
#         m = 1
#         l = len(matrix)-1
#         k = len(matrix)
#         while n <l:
#             for _ in range(k):
#                     if n <l:
#                         matrix[n][m], matrix[m][n]
#                         m += 1
#                         n += 1
#         for row in matrix:
            
        
        # print(matrix)
        # return matrix
            
        # for i in range(len(matrix)-1):
            
        # for i in range(len(matrix)):
        #     matrix[i].reverse()
            

obj = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(obj.rotate(matrix))



# n = 0

# while n <=4:
#     for i in range(n,4):
#         print(i)
#         n+=1