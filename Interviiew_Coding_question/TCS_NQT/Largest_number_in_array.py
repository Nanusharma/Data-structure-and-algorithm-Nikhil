class Solution():
    def largest(self,n)->int:
        largest = arr[0]
        for i in arr:
            if i > largest:
                largest= i
        return str(largest)
obj = Solution()
arr = [ 1,2,3,53,5,2,5,2,5,23,3,25,235,32,5,23,5,234,2345,23,4,234]
print(obj.largest(arr))