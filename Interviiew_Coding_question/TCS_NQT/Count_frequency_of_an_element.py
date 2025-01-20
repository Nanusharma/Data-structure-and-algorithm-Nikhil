class solution():
    def frequency_count(self, arr) -> list:
        hash_map = {}
        for i in arr:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for i in hash_map:
            print(f"Element: {i}, Frequency: {hash_map[i]}")


obj = solution()
arr = [ 1,2,3,53,5,2,5,2,5,23,3,25,235,32,5,23,5,234,2345,23,4,234]
print(obj.frequency_count(arr))