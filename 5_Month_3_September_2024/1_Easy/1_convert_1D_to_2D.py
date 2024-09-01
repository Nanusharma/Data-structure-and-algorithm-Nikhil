# https://leetcode.com/problems/convert-1d-array-into-2d-array/?envType=daily-question&envId=2024-09-01

from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m * n != len(original):
            return [] 
        
        array = []  
        length = len(original) 
        
        i = 0  
        while i < length:
            arr = original[i:i+n] 
            array.append(arr)  
            i += n 
        
        return array