class Solution():
    def __init__(self,value):
        self.data = value
        self.next= None

a = Solution(1)
b = Solution(2)
c = Solution(3)

a.next = b
b.next = c
c.next = a #circular linked list
print(b.next)