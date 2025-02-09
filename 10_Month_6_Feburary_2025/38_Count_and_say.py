# https://leetcode.com/problems/count-and-say/description/
class Solution:
    def countAndSay(self, n: int) -> str:
        a = 1
        S ="1"
        while a < n:
            def fxn1(S: str) -> list:
                count = 1
                ar = []
                for i in range(1, len(S)):
                    if S[i] == S[i-1]:
                        count += 1
                    else:
                        ar.append([count, int(S[i-1])])
                        count = 1
                ar.append([count, int(S[-1])])
                return ar

            def fxn(arr):
                S = ""
                for i in arr:
                    a = str(i[0])
                    b = str(i[1])
                    S= S+ a+b
                return S
  
            ar = fxn1(S)
            S = fxn(ar)
            a+=1
            # print(S)
        return S

obj = Solution()
n =4
print(obj.countAndSay(n))
