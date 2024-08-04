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
                        # row[j] = row[i] (aactually no need to flip)
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
                        # grid[j][c] = grid[i][c]
                        cols_flips += 1
                    i += 1
                    j -= 1
            return cols_flips
        
        row_flips = rows(grid)
        col_flips = cols(grid)
        

        return min(row_flips, col_flips)

obj = Solution()
grid= [[1,0,0],[0,0,0],[0,0,1]]
print(obj.minFlips(grid))  