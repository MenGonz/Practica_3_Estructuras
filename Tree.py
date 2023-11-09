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
        
    
    #Métodos básicos    
    def get_height(self): return self.height
    
    def get_root(self): return self.root
    
    def get_size(self): return self.size
    
    def is_empty(self): return not bool(self.get_root())
    
    
    
    #Métodos varios
    def insert(self, data):
        """
        Inserta una data en el árbol respetando la estructura.
        """
        if self.is_empty():
            self.root = Node(data)
        else:
            self.get_root().insert(data)
        
        self.height = self.root.get_height()
        self.size += 1
        
        
    def search(self, data) -> Node:
        """
        Busca un dato en el árbol y retorna (si existe) el nodo que lo contiene.
        """
        temp: Node = self.get_root()
        
        while temp:
            if temp.get_data() == data:
                return temp
            elif temp.get_data() > data:
                temp = temp.get_left()
            else:
                temp = temp.get_right()
                
        return None
    
    
    def remove(self, data):
        """
        Recibe un dato y remueve del árbol el nodo al que le corresponde.
        """
        nodo: Node = self.search(data)
        
        if nodo:
            if nodo.is_leaf() and not nodo.is_root():
                if nodo.get_parent().get_left() == nodo:
                    nodo.get_parent().l = None
                    nodo.p = None    
                elif nodo.get_parent().get_right() == nodo:
                    nodo.get_parent().r = None
                    nodo.p = None
            elif nodo.has_left():
                temp: Node = nodo.rightmost_node_of_left_subtree()
                nodo.data, temp.data = temp.data, nodo.data
                self.remove(temp)
            elif nodo.has_right():
                temp: Node = nodo.leftmost_node_of_right_subtree()
                nodo.data, temp.data = temp.data, nodo.data
                self.remove(temp)
        
            self.size -= 1
            self.height = self.get_root().get_height()
    
    
    
    def traverse(self, orden: str = "in") -> tuple[str]:
        """
        Retorna tupla con recorrido del árbol en el orden especificado.
        
        orden = "pre" | "in" | "pos" 
        """
        
        root: Node = self.get_root()
        recorrido: list[str] = []
        
        def visit(node: Node): recorrido.append(node.get_data())
        
        #funciones recursivas para recorrer el árbol
        def preorder(nodo: Node):
            """Recorrido RID"""
            visit(nodo)
            if nodo.has_left():
                preorder(nodo.get_left())
            if nodo.has_right():
                preorder(nodo.get_right())
        
        def inorder(nodo: Node):
            """Recorrido IRD"""
            if nodo.has_left():
                inorder(nodo.get_left())
            visit(nodo)
            if nodo.has_right():
                inorder(nodo.get_right())
        
        def posorder(nodo: Node):
            """Recorrido IDR"""
            if nodo.has_left():
                posorder(nodo.get_left())
            if nodo.has_right():
                posorder(nodo.get_right())
            visit(nodo)
        
        assert orden in {"in", "pre", "pos"}, "orden incorrecto"
        
        if orden == "pos":
            posorder(root)
        elif orden == "pre":
            preorder(root)
        else:
            inorder(root)
        
        return tuple(recorrido)
        
    
    #Métodos dunder
    def __str__(self):
        return f"""
Arbol binario de busqueda:
|   root: {self.get_root()}
|   size: {self.get_size()}
|   height: {self.get_height()}
|   nodos: {self.traverse()}
                """
        
    def __repr__(self):
        return f"{self.traverse()}"
        
    
if __name__ == "__main__":
    T: Tree = Tree()
    
    T.insert(2)
    T.insert(1)
    T.insert(3)
    T.insert(4)
    T.insert(0)
    
    
    print(T)
    