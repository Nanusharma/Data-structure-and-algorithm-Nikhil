# https://leetcode.com/problems/height-checker/description/?envType=daily-question&envId=2024-06-10
class Solution(object):
    def heightChecker(self, heights):
        # number of indices that does not match with the sorted heights
        
        count=0
        n = len(heights)
        unsorted_heights=[]
        unsorted_heights = heights[:]
        # sort
        for i in range(n):
            for j in range(0,n-i-1):
                if heights[j]>heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
                   
        for i in range(len(heights)):
            if unsorted_heights[i]== heights[i]:
                count+=1
        return count


sol = Solution()
heights = [2,1,3,5,4]
sol.heightChecker(heights)

'''
class Solution(object):
    def heightChecker(self, heights):
        # Sort the heights to get the expected order
        expected = sorted(heights)
        
        # Count the number of indices where the original heights differ from the expected heights
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        
        return count
'''