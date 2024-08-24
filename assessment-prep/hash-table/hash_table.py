class HashTable:
    def __init__ (self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, value):
        self.arr[self.get_hash(key)] = value
        
    def get(self, key):
        return self.arr[self.get_hash(key)]
    
    
t = HashTable()

t.add("march 6", 310)
t.add("march 7", 340)
t.add("march 8", 380)
t.add("march 9", 302)
t.add("march 10", 297)
t.add("march 11", 323)

print(t.get('march 10'))