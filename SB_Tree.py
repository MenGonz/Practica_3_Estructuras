
from Tree import Tree
from Node import Node

class BS_Tree(Tree):
    
    def __init__(self, key = None):
        super().__init__(key)
    
    #Métodos privados de la clase
        
    
    def insert(self,key):
        """Inserta un nodo con Tree.insert() y luego balancea."""
        n = super().insert(key)
        if n.get_depth() > 2:        
            n.get_parent().get_parent().balancear()
        
    def remove(self, key):
        """Remueve un nodo y luego balancea."""
        if (p := super().remove(key)):
            if not p.is_root():
                if not(p.get_parent().is_root()):
                    p.get_parent().balancear()
            
        
        
        


if __name__ == '__main__':
    T = BS_Tree()
    T.insert(1)
    T.insert(2)
    T.insert(3)
    T.insert(4)
    T.insert(5)
    T.insert(6)
    
    print(T)        
        