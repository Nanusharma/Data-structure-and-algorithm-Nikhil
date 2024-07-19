# class Solution(object):
#     def getEncryptedString(self, s, k):
#         n = len(s)
#         res=s+s   
#         p=" "
#         for i in range(n):
#             p+=res[i+k]
#         return p
# sol = Solution()
# s= "dart"
# k=3
# print(sol.getEncryptedString(s,k))

# class Solution(object):
#     def getEncryptedString(self, s, k):
#         n = len(s)
#         res = s + s  # Duplicate the string to handle wrapping around
#         p = ""  # Initialize the result string
#         for i in range(n):
#             p += res[i + k]  # Append the character at the shifted position
#         return p
    
# class Solution(object):
#     def getEncryptedString(self, s, k):
#         n = len(s)
#         k = k % n  # Ensure k is within the bounds of the string length
#         res = s + s  # Duplicate the string to handle wrapping around
#         p = ""  # Initialize the result string
#         for i in range(n):
#             p += res[i + k]  # Append the character at the shifted position
#         return p



# # 2#

# class Solution(object):
#     def numberOfSubmatrices(self, grid):
#         n = len(grid)
#         m = len(grid[0])
#         # print(grid[0,1])s
#         for i in grid:
#             for j in i:
#                 print(j)
#         sub_matrix = 

        
        
# sol = Solution()
# grid = [["X","Y","."],["Y",".","."]]
# print(sol.numberOfSubmatrices(grid))
# A= [5, 5, 5, 6, 6, 6, 8, 9]
# for i in range(A)