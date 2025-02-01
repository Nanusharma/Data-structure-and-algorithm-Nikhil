# # https://leetcode.com/problems/count-servers-that-communicate/?envType=daily-question&envId=2025-01-23

# from typing import List
# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         sum = 0 
#         for i in grid:
#             rows =0
#             prev = False
#             for j in i:
                
#                 if j ==1 and prev is True:
#                     rows+=1
#                 if j ==1 :
#                     prev = True
#             if prev == True and rows>0:
#                 rows+=1
#             print(rows)
#             # prev = False
#             sum+=rows
#         print(sum)
        
#         # p = len(grid)-1
#         # q = len(grid[0])-1
#         # i = 0 #len(grid)
#         # j = 0 #len(grid[0])
#         # columns = 0
#         # while j <= q and i <= p:
#         #     # print(grid[i][j])
#         #     if grid[i][j]== 1:
#         #         columns+=1
#         #         i+=1
#         #     elif i<=p:
#         #         j+=1
#         #         i+=1

#         # return sum+columns

# # [1,1,0,0],
# # [0,0,1,0],
# # [0,0,1,0],
# # [0,0,0,1]
# obj = Solution()
# grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# print(obj.countServers(grid))


for i in range(1,4):
    print(i)