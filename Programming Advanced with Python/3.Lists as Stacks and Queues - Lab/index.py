''' Lists as Stacks and Queues '''

''' What is Stack? :
- A stack is a linear data structure that stores items
- The process of adding data to a stack is referred to as a "push"
- Retrieving data from a stack is called a "pop"
- Elements in a stack are added/removed from the top ("last in, first out") or LIFO order
'''

''' Stack in Python :
The list methods make it very easy to use a list as a stack
To add an item to the top of the stack, use append()
To retrieve an item from the top of the stack, use pop()
'''
''' Stack methods'''
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# stack.pop()
# print(stack)


''' Time complexity : Python built-in data structures like list, sets, dictionaries provide a large number
of operations making it easier to write concise code but not being aware of their complexity can result in
unexpected slow behavior of your python code.
Important points:  

Lists are similar to arrays with bidirectional adding and deleting capability.
Dictionaries and Set use Hash Tables for insertion/deletion and lookup operations. '''


''' What is Queue? :
A queue is a first-in first-out (FIFO) abstract data type
We use them when we want things to happen in the order that they were called '''

''' Queues in Python: 
It is possible to use a list as a queue, however they are not efficient for this purpose
Doing inserts or pops from the beginning of a list is slow
That's why we use collections.deque
We use append() to add to the queue and popleft() to remove from the queue 
Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. 
Deque is preferred over a list in the cases where we need quicker append and pop operations from 
both the ends of the container, as deque provides an O(1) time complexity for append and pop operations 
as compared to a list that provides O(n) time complexity.'''

''' Deque can be used as stack and queues '''

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")        # Terry arrives
queue.append("Graham")       # Graham arrives
queue.popleft()              # First leaves: 'Eric'
queue.popleft()              # Second leaves: 'John'
print(queue)                 # ['Michael', 'Terry', 'Graham']

''' Deque methods '''
''' always we call collections and import deque '''

# initializing deque
de = deque([1, 2, 3, 4, 5, 6])
print("Current Deque: ", de)

# Accessing the front element of the deque
print("Front element of the deque:", de[0])

# Accessing the back element of the deque
print("Back element of the deque:", de[-1])

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3, ])

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4, 5, 6])

# printing modified deque
print("The deque after extending deque at end is : ")
print(de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to left end
de.extendleft([7, 8, 9])

# printing modified deque
print("The deque after extending deque at beginning is : ")
print(de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print("The deque after rotating deque is : ")
print(de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print("The deque after reversing deque is : ")
print(de)

