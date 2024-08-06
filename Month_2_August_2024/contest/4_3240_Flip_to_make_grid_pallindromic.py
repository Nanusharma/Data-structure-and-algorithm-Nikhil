# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/
from typing import List
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def rows(grid):
            rows_flips = 0
            for row in grid:
                i = 0
                j = len(row) - 1
                while i < j:
                    if row[i] != row[j]:
                        if row[j]==1:
                            row[i]=row[j]
                        else:
                            row[j] = row[i] 
                        rows_flips += 1
                    i += 1
                    j -= 1
            return rows_flips
        
        def cols(grid):
            cols_flips = 0
            num_cols = len(grid[0])
            num_rows = len(grid)
            for c in range(num_cols):
                i = 0
                j = num_rows - 1
                while i < j:
                    if grid[i][c] != grid[j][c]:
                        if grid[j][c]==1:
                            grid[i][c]=grid[j][c]
                        else:
                            grid[j][c] = grid[i][c]
                        cols_flips += 1
                    i += 1
                    j -= 1
            return cols_flips
        
        row_flips = rows(grid)
        col_flips = cols(grid)
        # def total_ones() -> int:
        #     return sum(sum(row) for row in grid)

        # row_flips = rows(grid)
        # col_flips = cols(grid)
        # ones_count = total_ones()
        
        # remainder = ones_count % 4
        # extra_flips = (4 - remainder) % 4
        
        total_flips =row_flips+col_flips 
        
        return total_flips
obj =Solution()
grid= [[0,1],[0,1],[0,0]]
print(obj.minFlips(grid))
