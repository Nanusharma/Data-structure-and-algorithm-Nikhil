# stack

stack = [i for i in range(0,10)]
for i in range(len(stack) - 1, -1, -1): #backward traversing
    print(stack[i])

for i in range(0,len(stack),1): #forward traversing
    print(stack[i])
print() #space
print(max(stack))

stack.append(4) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
stack.append(10) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 10]
stack.pop() #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
stack.pop() #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(stack)


# Queue
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)