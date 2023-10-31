from Node import Node


class Tree:
    
    root: Node
    height: int
    size: int
    
    def __init__(self, data= None):
        if data:
            self.root = Node(data)
            self.height = 1
            self.size = 1
        else:
            self.root = None
            self.height = 0
            self.size = 0
            
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.height = 1
        else:
            self.root.insert(data)
            self.height = self.root.height()
        self.size += 1
        
        
    def get_height(self):
        return self.height
    
    def get_root(self):
        return self.root.get_data()

