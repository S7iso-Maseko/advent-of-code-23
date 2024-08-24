class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None
        self.prev = None
    

class dl:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
            
        current = self.head
        while current.next:
            current = current.next
        
        current.next = newNode
        newNode.prev = current
        self.tail = newNode

    def ascending(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    def descending(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev      
    

dlist = dl()

dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.append(5)

dlist.ascending()
print("___________________")
dlist.descending()