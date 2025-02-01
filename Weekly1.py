# https://leetcode.com/problems/count-servers-that-communicate/?envType=daily-question&envId=2025-01-23

from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1
        
        return count

# Test cases
obj = Solution()
grid1 = [[1, 0], [0, 1]]
grid2 = [[1, 0], [1, 1]]
grid3 = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
print(obj.countServers(grid1))  # Output: 0
print(obj.countServers(grid2))  # Output: 3
print(obj.countServers(grid3))  # Output: 4