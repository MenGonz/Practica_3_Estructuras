

class Node:
    
    
    def __init__(self, data):
        self.data = data
        self.r: Node | None = None
        self.l: Node | None = None
        self.p: Node | None = None
        
    
    #privados
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
    
    
    #métodos varios
    def insert(self, data):
        if self.data > data:
            self.__insert_l(data)
        else:
            self.__insert_r(data)
            
    def is_leaf(self) -> bool:
        return self.get_right() is None and self.get_left() is None 
        
    def leftmost_node_of_right_subtree(self):
        temp: Node= self.get_right()
        while temp.get_left():
            temp = temp.get_left()

        return temp
    
    def rightmost_node_of_left_subtree(self):
        temp: Node = self.get_left()
        while temp.get_right():
            temp = temp.get_right()
            
        return temp
    
    
    #Getters y Setters
    
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
    def set_data(self, data):
        self.data = data
    
    def get_parent(self):
        return self.p
    def set_parent(self,nod):
        self.p = nod
    
    def get_right(self):
        return self.r
    def set_right(self,nod):
        self.r = nod
    
    def get_left(self):
        return self.l
    def set_left(self,nod):
        self.l = nod
    
    
    #Métodos dunder
    def __str__(self):
        return str(f"({self.data})")
    
    
    