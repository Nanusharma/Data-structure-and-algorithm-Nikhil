# reversing the array without using the extra space
class solution():
    def reverse_Array(self, arr) -> list:
        l = len(arr)-1
        L = len(arr)//2
        for i in range(L):
            
            arr[i],arr[l-i]= arr[l-i], arr[i]
            print(arr[i],arr[l-i])

        return arr


obj = solution()
arr = [0, 1,2,3,4,5,6,7,8,9,10]
print(obj.reverse_Array(arr))