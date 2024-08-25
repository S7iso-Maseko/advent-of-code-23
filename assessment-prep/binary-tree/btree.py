class bTree:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):        
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = bTree(data)
        
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = bTree(data)
        
    def inOrder(self, b): 
        # Need to implement this
        self
        

b = bTree(16)
b.insert(15)
b.insert(4)
b.insert(17)
b.insert(3)
b.insert(20)

b.inOrder(b)
        