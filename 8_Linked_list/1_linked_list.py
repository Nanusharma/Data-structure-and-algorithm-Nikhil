class LinkedList():
    def __init__(self):
        #create an empty linked list(linked list with no nodes )
        self.head=None # condition of linked list
        self.n = 0 #to count the nodes in the linked list


    def __len__(self):
        return self.n

#$ main operation in linked list 
# 1. insert [head, tail(list.append),middle(insert)]
# 2. traverse
# 3. delete(head, tail(pop),value(remove),index)
# 4. Search

L = LinkedList()
print(L)
print(len(L))