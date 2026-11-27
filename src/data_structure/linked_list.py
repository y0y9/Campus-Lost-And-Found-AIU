class Node :
    
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f"data : {self.data} \n "

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def __str__(self):
        if self.head is None:
            return "empty list"
        
        else:
            temp = self.head;
            output = []
            while temp:
                output.append(str(temp.data))
                temp = temp.next
            
            return '-->'.join(output)
    
    def __len__(self):
        return self.size
    
    
    def insert_end(self,data):
        new_node = Node(data,None)
        if self._size == 0 and self.head is None:
            self.head = new_node
            self._size += 1
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next;
    
        temp.next = new_node
        self._size +=1
        return;
    
    def insert_beginning(self,data):
        new_node = Node(data,None)
        if self._size == 0 and self.head is None:
            self.head = new_node
            self._size += 1
            return
        
        new_node.next = self.head;
        self.head = new_node
        self._size += 1 
        return
    
    
    def insert(self,data,index):
    
        if index < 0 or index > self._size :
            return False
        
        if index == 0 :
            self.insert_beginning(data=data)
            return True
        
        if index == self._size:
            self.insert_end(data=data)
            return True 

        else:
            new_node = Node(data,None)
            previous = None
            temp_index = 0
            temp = self.head
            
            while temp_index < index:
                previous = temp
                temp=temp.next
                temp_index += 1 
            previous.next = new_node
            new_node.next = temp
            self._size += 1
            return True
    
    def delete(self,data):
        
        if self.head is None :
            return False
        
        if self.head.data == data :
            self.head = self.head.next
            self._size -= 1
            return True
        temp = self.head
        
        while temp.next :
            if temp.next.data == data :
                temp.next = temp.next.next
                self._size -= 1
                return True
            temp = temp.next
        return False
    
    def search(self, data):
        
        temp = self.head 
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next;
        return None;
    
    def get(self,index):
        if index < 0 or index > self._size :
            raise IndexError("Index out of range")
        temp = self.head
        temp_index = 0
        while temp_index < index :
            temp = temp.next;
            temp_index += 1
        return temp
    
    def size(self):
        return self._size
    
    def is_empty(self):
        return self.head is None
    
    def clear(self):
        self._size = 0
        self.head = None