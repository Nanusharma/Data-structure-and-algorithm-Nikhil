class Solution(object):
   
    def subarraysDivByK(self, nums, k):
        n=len(nums)
        count=0
        for i in range(n):
            # print(i)
            for j in range(i,n):
                # print(j)
                subarray_sum=0
                for l in range(i,j+1):
                    subarray_sum+=nums[l]
                    print(subarray_sum)
                    if subarray_sum%k==0:
                        count+=1
        print(count)
            
        
        if len(nums)==1 and nums[0]%k ==0:
            return 1
        if len(nums)==1 and nums[0]%k !=0:
            return 0
sol =Solution()
nums = [4,5,0,-2,-3,1]
k = 5     
sol.subarraysDivByK(nums,k)           