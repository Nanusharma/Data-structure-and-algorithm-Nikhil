# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

class Solution:
    def maxScore(self, s: str) -> int:
        array = [ ]
        for i in s:
            array.append(int(i))
        l = len(array)
        count = 0 
        for i in range(l-1):
            left = array[0:i+1]
            right = array[i+1:l]
            zeros = sum(1 for count in left if count == 0)
            ones = sum(1 for count in right if count == 1)
            count= max(zeros+ones,count)
        return count

obj = Solution()
s = "1111"
print(obj.maxScore(s))

