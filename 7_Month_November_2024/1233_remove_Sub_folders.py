# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/submissions/1439029765/?envType=daily-question&envId=2024-10-25
from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        result = []
        prev = None  # Store the previous kept folder

        for f in folder:
            # If it's the first folder or f is not a subfolder of prev, add it to result
            if prev is None or not f.startswith(prev + '/'):
                result.append(f)
                prev = f  # Update the previous folder to the current one

        return result

obj = Solution()
folder = ["/a","/c/d","/c/d/e","/c/f","/a/b"]
# ['a', 'ab', 'cd', 'cde', 'cf']
print(obj.removeSubfolders(folder))   