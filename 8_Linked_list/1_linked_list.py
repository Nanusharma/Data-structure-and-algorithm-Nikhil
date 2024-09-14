# # class Node():
# #     def __init__(self,value):
# #         self.data = value
# #         self.head = None
# # class LinkedList():
# #     def __init__(self):
# #         #create an empty linked list(linked list with no nodes )
# #         self.head=None # condition of linked list
# #         self.n = 0 #to count the nodes in the linked list


# #     def __len__(self):
# #         return self.n

# # #$ main operation in linked list 
# # # 1. insert [head, tail(list.append),middle(insert)]
# # # 2. traverse
# # # 3. delete(head, tail(pop),value(remove),index)
# # # 4. Search
    

# #     def insert_head(self, value):
# #         new_node = Node(value)
# #         new_node.next = self.head
# #         self.head = new_node
# #         self.n = self.n+1

# # L = LinkedList()
# # L.insert_head(1)
# # L.insert_head(2)
# # L.insert_head(3)
# # L.insert_head(4)

# # print(L)
# # print(len(L))




class A():
    def disp(self):
        print("a disp()")
class B(A):
    pass
obj = B()
obj.disp()