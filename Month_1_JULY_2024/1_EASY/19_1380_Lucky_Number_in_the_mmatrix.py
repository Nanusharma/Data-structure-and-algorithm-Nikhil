# https://leetcode.com/problems/lucky-numbers-in-a-matrix/submissions/1326430509/?envType=daily-question&envId=2024-07-19
from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins_in_row =[]
        maxs_in_column=[]
        for row in matrix:
            mins_in_row.append(min(row))
        for i in range(len(matrix[0])): 
            max_in_column=0
            for j in range (len(matrix)):  
                max_in_column = max(max_in_column, matrix[j][i])
            maxs_in_column.append(max_in_column)
        
        Lucky_Number=set(mins_in_row) & set(maxs_in_column)
        print(mins_in_row)
        print(maxs_in_column)
        return list(Lucky_Number)
obj= Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(obj.luckyNumbers(matrix))


# chatgpt

from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_in_row = []
        max_in_column = []

        # Find the minimum in each row
        for row in matrix:
            min_in_row.append(min(row))

        # Find the maximum in each column
        for col in range(len(matrix[0])):
            max_in_column.append(max(row[col] for row in matrix))

        # Find the intersection of min_in_row and max_in_column
        lucky_numbers = set(min_in_row) & set(max_in_column)
        
        return list(lucky_numbers)