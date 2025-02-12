from typing import List
from collections import defaultdict
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])
                print()
                print(diagonals)
        for key in diagonals:
            if key >= 0:
                diagonals[key].sort(reverse=True) 
            else:
                diagonals[key].sort()  
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)
        return grid