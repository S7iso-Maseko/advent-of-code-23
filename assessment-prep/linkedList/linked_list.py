class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def append(self, data):        
        if self.head is None:
            self.head = Node(data)
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = Node(data)
        
    def listValues(self):
        nextNode = self.head
        llstr = ''
        while nextNode:
            llstr += str(nextNode.data) + ' ---> '
            nextNode = nextNode.next
            
        print(llstr + 'None')
        
    def insert_after_value(self, data_after, new_data):
        node = Node(new_data)
            
        current = self.head
        while current:
            if data_after == current.data:
                 node.next = current.next
                 current.next = node
                 break
            current = current.next
    
    def remove_by_value(self, data):
        if self.head is None:
           print("It Can Never") 
           return
        
        if self.head.data == data:
            self.head = self.head.next
            return
       
        current = prev = self.head
        while current:
            if data == current.data:
                prev.next = current.next
                return
            
            prev = current
            current = current.next
           
        
            

llist = Linkedlist()
llist.append(3)
llist.append(1)
llist.append(2)
llist.append(5)
llist.append(8)

llist.insert_at_begining(389)

llist.insert_after_value(1, 87)

llist.remove_by_value(389)

llist.listValues()