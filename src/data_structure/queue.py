class Node:
    
    def __init__(self, claim):
        self.claim = claim
        self.next = None

class Queue:
  
    def __init__(self):
        self._front = None
        self._rear = None
        self._count = 0

    def enqueue(self, claim):
        
        new_node = Node(claim)

        if self._rear is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node

        self._count += 1

    def dequeue(self):
        
        if self.is_empty():
            return None

        removed_node = self._front
        self._front = self._front.next

        if self._front is None:
            self._rear = None

        self._count -= 1
        return removed_node.claim

    def peek(self):
       
        if self.is_empty():
            return None
        return self._front.claim

    def is_empty(self):
        return self._front is None

    def size(self):
        return self._count

    def clear(self):
       
        self._front = None
        self._rear = None
        self._count = 0
