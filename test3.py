class Solution:
    # def minInsertions(self, s: str) -> int:
    #     left = 0 
    #     right = len(str)-1
    #     count=0
    #     for i in range(len(str)):
    #         if str[left]!=str[right]:
    #             count+=1
    #         else:
    #             left += 1
    #             right -= 1
    def make_palindrome(s):
        left = 0
        right = len(s) - 1
        count = 0
        while left < right:
            if s[left] != s[right]:
                s = s[:right + 1] + s[left] + s[right + 1:]

                count += 1
            # Update the right pointer due to the new insertion
                right += 1
            else:
            # If characters match, move both pointers inward
                left += 1
                right -= 1

        return count

        # while left <= right:
        #     print(left)
        #     print(right)
        #     print()
        #     if str[left]!=str[right]:
        #         left += 1
        #         right -= 1
        #         count+=1
        #     else:
        #         left += 1
        #         right -= 1
        # return count
        
obj= Solution()
# str ='leetcode'
s='zaz'
# str='mbadm'
print(obj.make_palindrome(s))
    # leetcode
    # leetcodel
    # leetcodeel
    # leetcodteel
    # leetcodcteel
    # leetcodocteel