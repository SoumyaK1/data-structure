##### Stack using deque ( The best way in non-threaded environment. Deque is thread-safe if it only uses push (append) and pop operations)
from collections import deque
## The below class extends deque class and defines new functions for peek and empty
class Stack(deque):
    def __init_(self):
        None
    def peek(self):
        l = len(self)
        return self[l-1]
    def isEmpty(self):
        val = False if len(self) else True
        return val
myStack = Stack() ## Build an empty stack
myStack.append(10) ## push an item to the stack
myStack.append(34)
myStack.append(1)
myStack.append(2)
myStack.append(78)

mystack.pop() ## pop top element from stack

mystack.peek() ## peek the top element

mystack.isEmpty() ## check if the stack is Empty

##### Stack using LifoQueue : It is thread-safe. So the best to use in multi-threaded environment under the cost of a little bit processing over-head.

from queue import LifoQueue
myStack = LifoQueue() 
##myStack = LifoQueue(10) ## Defines stack size

myStack.put(1)
myStack.put(11)
myStack.put(7)
myStack.put(18)
myStack.put(5)

myStack.put_nowait() ## Use this if the stack is created with a predefined size. get_nowait() Throws error message if the stack is full

myStack.get_nowait() ## USe this instaed of get() becuase get_nowait() throws error message if the stack is Empty

mystack.empty() ## check if the stack is empty
myStack.full() ## check if the stack is full()
print(myStack.queue) ## Print the contnts of the stack






