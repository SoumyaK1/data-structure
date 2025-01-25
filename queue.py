#### Queue using dequeue

from collections import deque
class Queue:
    def __init__(self,*elements):
        self._items = deque(elements)
    def enqueue(self,item):
        self._items.appendleft(item)
    def dequeue(self):
        return self._items.pop()
    def __str__(self):
        s = ''
        for e in self._items:
            s = s+str(e)+','
        return '['+s[:-1]+']'
    def size(self):
        return len(self._items)
    def isEmpty(self):
        return False if len(self._items) else True
    def peek(self):
        l = len(self._items)
        return self._items[l-1]

que = Queue(1,4,7,1,9,10)
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)

que.dequeue()
    
        
