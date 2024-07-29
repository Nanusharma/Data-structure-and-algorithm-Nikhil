# class Solution:
#     def make_palindrome(self,s):
#         left = 0
#         right = len(s) - 1
#         count = 0
#         while left < right:
#             if s[left] != s[right]:
#                 s = s[:right + 1] + s[left] + s[right + 1:]
#                 count += 1
#                 right += 1
#             else:
#                 left += 1
#                 right -= 1
#         return count
        
# obj= Solution()
# # str ='leetcode'
# s='zaz'
# # str='mbadm'
# print(obj.make_palindrome(s))
    # leetcode
    # leetcodel
    # leetcodeel
    # leetcodteel
    # leetcodcteel
    # leetcodocteel\\

class Solution:
    def make_palindrome(self, s):
        left = 0
        right = len(s) - 1
        str_len = len(s)
        count=0
        s2 = list(s) 
        while left < right:
            if s2[left] != s2[right]:
                s2.insert(right + 1, s2[left])
                count += 1
                right += 1
            else:
                left += 1
                right -= 1
        leng= len(s2)-str_len
        return count,s,leng

obj = Solution()
# s = 'zaz'
# s ='leetcode'
# s='zaz'
# s='mbadm'
s="zjveiiwvc" # outpot = 8 , ex
print(obj.make_palindrome(s))

# "zjveiiwvc"
# zjveiiwvcz
# zjveiiwvcjz