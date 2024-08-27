class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
        
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
        
def preorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.data, end=' ')
        
if __name__ == "__main__":
    
    root = Node(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    
    print("InOrder")
    inorder(root)
    print("")
    preorder(root)