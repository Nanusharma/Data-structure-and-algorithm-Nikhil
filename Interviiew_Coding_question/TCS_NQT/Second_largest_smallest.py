class Solution:
    def second_smallest_largest(self, arr) -> list:
        if len(arr) < 2:
            return [None, None, None, None]

        smallest = float('inf')
        second_smallest = float('inf')
        largest = float('-inf')
        second_largest = float('-inf')

        for i in arr:
            if i < smallest:
                second_smallest = smallest
                smallest = i
            elif i < second_smallest and i != smallest:
                second_smallest = i

            if i > largest:
                second_largest = largest
                largest = i
            elif i > second_largest and i != largest:
                second_largest = i

        return [second_largest, second_smallest]

obj = Solution()
arr = [2345, 1, 2, 3, 53, 5, 2, 5, 2, 5, 23, 3, 25, 235, 32, 5, 23, 5, 234, 2345, 23, 4, 234]
print(obj.second_smallest_largest(arr))
