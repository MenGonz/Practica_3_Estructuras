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
    
    def search(self, data) -> Node:
        temp = self.root
        while temp:
            if temp.get_data() == data:
                return temp
            elif temp.get_data() > data:
                temp = temp.get_left()
            else:
                temp = temp.get_right()
        return None
    
    
    def delete(self, data):
        nodo = self.search(data)
        
        if nodo:
            if nodo.is_leaf():
                if nodo.get_parent().get_left() == nodo:
                    nodo.get_parent().l = None
                    nodo.p = None
                else:
                    nodo.get_parent().r = None
                    nodo.p = None
                    
            elif nodo.get_left() is not None:
                temp = nodo.rightmost_node_of_left_subtree()
                nodo.data, temp.data = temp.data, nodo.data
                self.delete(temp)
            else:
                temp = nodo.leftmost_node_of_right_subtree()
                nodo.data, temp.data = temp.data, nodo.data
                self.delete(temp)
                
    
                
    