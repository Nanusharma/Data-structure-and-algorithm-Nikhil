# https://leetcode.com/problems/reorganize-string/description/


# class Solution(object):
#     def reorganizeString(self, s):
#         hash_table={}
#         count=0
#         count_2=0
#         for i in s:
#             if i in hash_table:
#                 hash_table[i]+=1
#                 count+=1
#             else: 
#                 hash_table[i]=1
#                 count+=1
#         for i in hash_table:
#             count_2+=1
#         print(count)
#         print(count_2)
#         print(s.append("a"))

# sol=Solution()
# # s="aab"
# s="aaab"
# print(sol.reorganizeString(s))



# import heapq

# class Solution(object):
#     def reorganizeString(self, s):
#         s_list= list(s)
#         hash_table={}
#         heapq.heapify(s_list)
#         count=0
#         count_2=0
#         for i in s_list:
#             if i in hash_table:
#                 hash_table[i]+=1
#                 count+=1
#             else: 
#                 hash_table[i]=1
#                 count+=1
#         alternate_s=[]
#         index=0
#         while s_list:
#             char=heapq.heappop(s_list)
#             if index%2==0:
#                 alternate_s.append(char)
#             index+=1
#         return ''.join(alternate_s)

# sol=Solution()
# # s="aab"
# s="aaab"
# print(sol.reorganizeString(s))

import heapq

class Solution(object):
    def reorganizeString(self, s):
        s_list= list(s)
        hash_table={}
        heapq.heapify(s_list)
        count=0
        count_2=0
        for i in s_list:
            count+=1
        alternate_s=[]
        index=0
        while s_list:
            char=heapq.heappop(s_list)
            if index%2==0:
                alternate_s.append(char)
            index+=1
        if len(alternate_s)== len(s):
            return ''.join(alternate_s)
        else:
            return ""
sol=Solution()
# s="aab"
s="aaab"
print(sol.reorganizeString(s))