class Solution():
    def smallest(self,n)->int:
        smallest = arr[0]
        for i in arr:
            if i < smallest:
                smallest= i
        return str(smallest)
obj = Solution()
arr = [ 1,2,3,53,5,2,5,2,5,23,3,25,235,32,5,23,5,234,2345,23,4,234]
print(obj.smallest(arr))