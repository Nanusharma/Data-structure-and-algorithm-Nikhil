# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/description/


# print(f"value of i,j: {i,j}")
# grid = [[3,2,1],[2,1,0],[1,2,3]]
# grid = [[3,2],[1,3],[3,4],[0,1]]
# grid= [[50],[0]]
# grid = [[0]]

from typing import List
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        count=0
        i,j=0,0
        m = len(grid[0]) # number of columns 2
        n = len(grid) # number of rows 1
        print(m,n)
        if m==1 and n==1:
            return 0
        else:
            while j<m:
                for i in range(n):
                    # print(f"value of i,j: {i,j}")
                    if i <n-1:
                        while grid[i][j]<=grid[i+1][j]:
                            grid[i][j]+=1
                            count+=1
                    if i == n -1:
                        while grid[i][j]<=grid[i-1][j]:
                            grid[i][j]+=1
                            count+=1
                j+=1    
        return count
    
obj = Solution()
grid=[[50,0]]
print(obj.minimumOperations(grid))