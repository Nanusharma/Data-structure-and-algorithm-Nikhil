# https://leetcode.com/problems/grid-game/description/?envType=daily-question&envId=2025-01-21
from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Calculate prefix sums for both rows
        for i in range(2):
            for j in range(1, n):
                grid[i][j] += grid[i][j - 1]
        
        # Initialize the result to a large number
        result = float('inf')
        
        # Iterate through each possible column where the first robot can switch rows
        for j in range(n):
            # Points collected by the second robot if the first robot switches at column j
            top = grid[0][n - 1] - grid[0][j] if j < n - 1 else 0
            bottom = grid[1][j - 1] if j > 0 else 0
            result = min(result, max(top, bottom))
        
        return result

grid = [[2, 5, 4], [1, 5, 1]]
# grid = [[3, 3, 1], [8, 5, 2]]
grid = [[20, 3, 20, 17, 2, 12, 15, 17, 4, 15], [20, 10, 13, 14, 15, 5, 2, 3, 14, 3]] # expected 63
# grid = [[1, 3, 1, 15], [1, 3, 3, 1]]
print(Solution().gridGame(grid))












# # https://leetcode.com/problems/grid-game/description/?envType=daily-question&envId=2025-01-21
# from typing import List
# class Solution:
#     def gridGame(self, grid: List[List[int]]) -> int:
#         print(grid[0])
#         print(grid[1])
#         print()
#         l = len(grid[0])
#         for i in range(2):
#             sum = 0
#             for j in range(l):
#                 sum += grid[i][j]
#                 grid[i][j]=sum

#         prefix_1= grid[0][l-1]
#         prefix_2 = grid[1][l-1]
 
#         print(grid[0])
#         print(grid[1])
#         print()

#         i, j = 0, 0 
#         pivotIndex = 0
#         pivotIndex2= 0
#         while j <= l-1 and i < 2:
#             if j>0 :
#                 first = grid[i][j-1]
#             else:
#                 first = 0
#             S1 = prefix_1 - grid[i][j] > prefix_2-first
#             print(S1)
#             # for right operation   
#             if i==2 and j ==l-1:
#                 grid[2][l-1]=0
#             if S1 is True :
#                 if j<=l-1:
#                     pivotIndex = grid[i][j]
#                     pivot_i = i
#                     pivot_j = j
#                     pivotIndex2 = grid[i+1][j]
#                     grid[i][l-1] = grid[i][l-1] - grid[i][j]
#                     grid[i][j] = 0
#                     j+=1

#             else:
#                 pivotIndex = grid[i][j]
#                 pivot_i = i
#                 pivot_j = j
#                 pivotIndex2 = grid[i+1][j]
#                 grid[i][l-1] = grid[i][l-1] - grid[i][j]
#                 grid[i][j] = 0
#                 i+=1
                
#                 while j <=l-1:
#                     grid[i][l-1] = grid[i][l-1] - grid[i][j]
#                     grid[i][j] = 0
#                     j+=1
#         grid[1][l-1]= 0
#         print(grid[0])
#         print(grid[1])
#         print()

#         i, j = pivot_i, pivot_j
#         print(i,j)
    
#         if (i+j) <=l//2:
#             sum = 0
#             grid[0][l-1] = prefix_1
#             for i in grid[0]:
#                 i = i-sum
#                 sum+=i
#             return sum-pivotIndex
#         else:
#             sum = grid[1][i]
#             for i in range(1,l):
#                 if grid[1][i]!= 0:
#                     a = grid[1][i] - grid[1][i-1]
#                     sum+=abs(a)
#             return sum
                
# obj =Solution()

# grid = [[2,5,4],[1,5,1]]
# # grid = [[3,3,1],[8,5,2]]
# grid = [[20, 3, 20, 17, 2, 12, 15, 17, 4, 15], [20, 10, 13, 14, 15,  5,2, 3, 14, 3]]
# # grid = [[1,3,1,15],[1,3,3,1]]
# print(obj.gridGame(grid))