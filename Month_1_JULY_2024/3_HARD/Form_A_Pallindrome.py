class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        count = 0
        s = list(s)  # convert string to list
        while left < right:
            if s[left] != s[right]:
                s.insert(right + 1, s[left])
                count += 1
                right += 1
            else:
                left += 1
                right -= 1
        return count

# input = "zjveiiwvc"
# output= 5
# expected =5
        

obj= Solution()
# str ='leetcode'
# str='zaz'
# str='mbadm'
str= "zjveiiwvc"
print(obj.minInsertions(str))
    # leetcode
    # leetcodel
    # leetcodeel
    # leetcodteel
    # leetcodcteel
    # leetcodocteel
    
