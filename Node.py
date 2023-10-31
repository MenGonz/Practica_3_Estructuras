

class Node:
    
    def __init__(self, data):
        self.data = data
        self.r = None
        self.l = None
        self.p = None
        
    
    def __insert_r(self, data):
        if self.r is None:
            self.r = Node(data)
        else:
            self.r.insert(data)
            
    def __insert_l(self, data):
        if self.l is None:
            self.l = Node(data)
        else:
            self.l.insert(data)
    
    def insert(self, data):
        if self.data > data:
            self.__insert_l(data)
        else:
            self.__insert_r(data)
    
    def get_height(self) -> int:
        if self.r is None and self.l is None:
            return 1
        elif self.r is None:
            return 1 + self.l.get_height()
        elif self.l is None:
            return 1 + self.r.get_height()
        else:
            return 1 + max(self.r.get_height(), self.l.get_height())
        
    def get_depth(self) -> int:
        if self.p is None:
            return 0
        else:
            return 1 + self.p.depth()
        
    def get_data(self):
        return self.data
    
    def get_parent(self):
        return self.p
    
    def get_right(self):
        return self.r
    
    def get_left(self):
        return self.l
    
    def set_data(self, data):
        self.data = data
    
    def __str__(self):
        return str(f"({self.data})")
    
    
    