# https://leetcode.com/problems/longest-palindrome/


'''class Solution(object):
    def longestPalindrome(self,s):
        hash_table= {}
        count=0
        count_1=0
        count_3=0
        for i in s:
            if i in hash_table:
                hash_table[i]+=1
            else:
                hash_table[i]=1
        for i in hash_table:
            if hash_table[i]%2==0:
                count+=hash_table[i]
            elif len(hash_table)==1:
                count_3 += hash_table[i]    
            elif hash_table[i]==1:
                count_1+=1   
        val=count+1 if count_1>=1 else count
        return count_3 if len(hash_table)==1 else val    
sol=Solution()
s="a"
print(sol.longestPalindrome(s))
'''



class Solution(object):
    def longestPalindrome(self, s):
        hash_table = {}
        count = 0
        count_1 = 0
        for i in s:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1
        for i in hash_table:
            if hash_table[i] >= 2:
                count += (hash_table[i] // 2) * 2 
                hash_table[i] %= 2 
            if hash_table[i] == 1:
                count_1 = 1 
        val = count + count_1

        return val           

sol=Solution()
s="abccccdd"
print(sol.longestPalindrome(s))