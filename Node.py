

class Node:
    
    
    def __init__(self, key):
        self.key = key
        self.r: Node | None = None
        self.l: Node | None = None
        self.p: Node | None = None
        
    
    #Méodos privados de la clase
    def __insert_r(self, key):
        if not self.has_right():
            n: Node = Node(key) 
            self.r = n
            n.p = self
            return n
        else:
            return self.r.insert(key)
            
    def __insert_l(self, key):
        if not self.has_left():
            n: Node = Node(key) 
            self.l = n
            n.p = self
            return n
        else:
            return self.l.insert(key)
    
    
    #métodos varios
    def balancear(self):
        """
        Balancea los subárboles del vértice
        """
        if not self.is_root():
            if self.balance_factor() == 2:
                if self.get_right().balance_factor() == -1:
                    self.get_right().right_rotate()
                else:
                    self.left_rotate()
            elif self.balance_factor() == -2:
                if self.get_left().balance_factor() == 1:
                    self.get_left().left_rotate()
                else:
                    self.right_rotate()    
            self.get_parent().balancear()
        else:
            ...
        
                
    
    def left_rotate(self):
        """Realiza una rotación izquierda del nodo."""
        if self.has_right():
            x = self
            y = self.get_right()
            if not self.is_root():
                if self.get_parent().get_right() == x:
                    self.p.r = y
                else:
                    self.p.l = y
            self.r = y.l
            y.l = x
            y.p = x.p
    
    def right_rotate(self):
        """Realiza una rotación derecha del nodo."""
        if self.has_left():
            x = self
            y = self.get_left()
            if not self.is_root():
                if self.get_parent().get_right() == x:
                    self.p.r = y
                else:
                    self.p.l = y
            self.l = y.r
            y.r = x
            y.p = x.p
    
    def balance_factor(self):
        if self.is_leaf():
            return 0
        elif not self.has_right():
            return -1 - self.get_left().get_height()
        elif not self.has_left():
            return 1 + self.get_right().get_height()
        else:
            return self.get_right().get_height() - self.get_left().get_height()
    
    def insert(self, key):
        """
        Le inserta un hijo al subárbol apropiado debajo de el nodo.
        """
        if self.key > key:
            n = self.__insert_l(key)
        else:
            n = self.__insert_r(key)
        return n
        
               
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
            return 1 + self.p.get_depth()
        
    def get_key(self): return self.key
    def set_key(self, key): self.key = key
    
    def get_parent(self): return self.p
    def set_parent(self,nod): self.p = nod
    
    def get_right(self): return self.r
    def set_right(self,nod): self.r = nod
    
    def get_left(self): return self.l
    def set_left(self,nod): self.l = nod
    
    
    #Métodos dunder
    def __str__(self):
        return str(self.get_key())
    
    def __repr__(self):
        return f"""({self.get_left()} <- {self} -> {self.get_right()})"""
    
    