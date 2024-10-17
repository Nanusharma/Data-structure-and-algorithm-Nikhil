# # https://leetcode.com/problems/string-to-integer-atoi/?envType=problem-list-v2&envId=string
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         array = [str(i) for i in range(10)]+['+','-','.','']
#         numbers = ""
#         s = s.replace(" ", "")
#         for i in s:
#             if i not in array:
#                 break
#             if i ==0 and s[i]==0:
#                 pass
#             if i in array:
#                 numbers= numbers+i
#                 print(numbers)
        
#         if numbers == "":
#             return 0
#         else:
#             return int(numbers)
class Solution:
    def myAtoi(self, s: str) -> int:
        array = [str(i) for i in range(10)]
        array2= ['+','-','.','']
        numbers = ""
        
        s = s.replace(" ", "")
        print(s)
        
        for i in s:
            if i not in array:
                break
            if i in array and i not in array2:
                numbers= numbers+i
            if i in array2 and i > 0 and numbers=="":
                numbers= numbers+i
                
        
        if numbers == "":
            return 0
        else:
            return int(numbers)
obj = Solution()
s = " -042" 
s= "42"
s= "1337c0d3"
s ="   -042"
# s ="0-1"
print(obj.myAtoi(s))