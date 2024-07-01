class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        # First sort arr2, so that the elements that are not in arr1 are 
        # in sorted order at the end of the relative sorted array
        n = len(arr2)  # sort
        relative = []
        remaining = []
        
        # Hash table to count occurrences in arr1
        # hash_table
        value_counts = {}
        for value in arr1:
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1
        # print(value_counts)
        # swap
        for value in arr2:
            if value in value_counts:
                relative.extend([value] * value_counts[value])
                del value_counts[value]
        

        for num in value_counts:
            remaining.extend([num] * value_counts[num])
        remaining.sort()
        relative.extend(remaining)
        
        return relative


# Example usage:
solution = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(solution.relativeSortArray(arr1, arr2))  # Output: [2,2,2,1,4,3,3,9,6,7,19]
