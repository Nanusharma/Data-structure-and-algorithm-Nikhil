# https://leetcode.com/problems/count-the-number-of-special-characters-i/
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hash_map={}
        for i in word:
            hash_map[i]=True
        arr=[]
        count=0
        for i in hash_map:
            arr.append(i) # basically a set
        for char in arr:
            if 'a' <= char <= 'z':  # Manual check if char is lowercase
                corresponding_upper = chr(ord(char) - 32)  # Convert to uppercase
                if corresponding_upper in arr:
                    count += 1
        
        return count