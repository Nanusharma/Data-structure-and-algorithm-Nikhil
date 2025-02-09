# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/description/


# print(f"value of i,j: {i,j}")
# grid = [[3,2,1],[2,1,0],[1,2,3]]
# grid = [[3,2],[1,3],[3,4],[0,1]]
# grid= [[50],[0]]
# grid = [[0]]

from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid[0])  # Number of columns
        n = len(grid)     # Number of rows

        # Iterate through each column
        for j in range(m):
            for i in range(1, n):
                if grid[i][j] <= grid[i-1][j]:
                    increment = grid[i-1][j] - grid[i][j] + 1
                    grid[i][j] += increment
                    count += increment

        return count
    
obj = Solution()
grid=[[50,0]]
print(obj.minimumOperations(grid))