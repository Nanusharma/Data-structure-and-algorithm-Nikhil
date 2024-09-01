from typing import List
import time
class Solution:
    # class Solution:
    
    def nonSpecialCount(self, l: int, r: int) -> int:
        count_1=0
        for i in range(l,r+1):
            count=0
            for j in range(1,i):
                if i%j==0:
                    count+=1
                    if count==2:
                        break
            if count==2:
                count_1+=1
        return (r+1)-l-count_1        

obj = Solution()
l=364
r= 21316
# 20927
start_time = time.time()
result = obj.nonSpecialCount(l, r)
end_time = time.time()
print(f"Result: {result}")
print(f"Execution time: {end_time - start_time} seconds")


'''
def 


'''