from collections import deque


class Queue:

   
    def is_empty(self):
       
        return len(self._items) == 0

    def __init__(self):
        self._items = deque()

    def enqueue(self, claim):
        
        self._items.append(claim)

    def dequeue(self):
        
        if self.is_empty():
            return None
        return self._items.popleft()

    def peek(self):
        
        if self.is_empty():
            return None
        return self._items[0]

    def size(self):
        
        return len(self._items)

    def clear(self):
       
        self._items.clear()
