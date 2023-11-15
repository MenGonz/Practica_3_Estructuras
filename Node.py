from User import User

class Node:
    
    
    def __init__(self, key:int,data ):
        self.key: int = key
        self.data = data
        self.r: Node | None = None
        self.l: Node | None = None
        self.p: Node | None = None
        
    
    #Méodos privados de la clase
    def __insert_r(self, key, data):
        if not self.has_right():
            n: Node = Node(key, data) 
            self.r = n
            n.p = self
        else:
            self.r.insert(key, data)
            
    def __insert_l(self, key, data):
        if not self.has_left():
            n: Node = Node(key, data) 
            self.l = n
            n.p = self
        else:
            self.l.insert(key, data)
    
    
    #métodos varios
    def insert(self, key, data):
        """
        Le inserta un hijo al subárbol apropiado debajo de el nodo.
        """
        if self.key > key:
            self.__insert_l(key, data)
        else:
            self.__insert_r(key, data)
               
    def has_left(self) -> bool: return bool(self.get_left())
    
    def has_right(self) -> bool: return bool(self.get_right())    
    
    def is_leaf(self) -> bool: return not( self.has_left() or self.has_right()) 
    
    def is_root(self) -> bool: return not bool(self.get_parent())
    
    def leftmost_node_of_right_subtree(self):
        """
        Retorna el descendiente más pequeño del sub-árbol derecho del nodo.
        """
        temp: Node= self.get_right()
        while temp.get_left():
            temp = temp.get_left()

        return temp
    
    def rightmost_node_of_left_subtree(self):
        """
        Retorna el descendiente más grande del sub-árbol derecho del nodo.
        """
        temp: Node = self.get_left()
        while temp.get_right():
            temp = temp.get_right()
            
        return temp
    
    
    
    #Getters y Setters
    
    def get_height(self) -> int:
        
        if self.is_leaf():
            return 1
        elif not self.has_right():
            return 1 + self.get_left().get_height()
        elif not self.has_left():
            return 1 + self.get_right().get_height()
        else:
            return 1 + max(self.r.get_height(), self.l.get_height())
        
    def get_depth(self) -> int:
        if self.is_root():
            return 0
        else:
            return 1 + self.p.depth()
        
    def get_key(self): return self.key
    def set_key(self, key): self.key = key
    
    def get_data(self): return self.data
    def set_data(self, data): self.data = data
    
    def get_parent(self): return self.p
    def set_parent(self,nod): self.p = nod
    
    def get_right(self): return self.r
    def set_right(self,nod): self.r = nod
    
    def get_left(self): return self.l
    def set_left(self,nod): self.l = nod
    
    
    #Métodos dunder
    def __str__(self):
        if self.isinstance(User):
            return f"<{self.get_data()} | {self.get_key()}>"
        return str(self.get_data())
    
    def __repr__(self):
        return f"""({self.get_left()} <- {self} -> {self.get_right()})"""
    
    