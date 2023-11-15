from Node import Node


class Tree:
    
    root: Node
    height: int
    size: int
    PRINT_INDT = 1
    
    def __init__(self, key: int = None, data= None):
        if key and data:
            self.root = Node(key, data)
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
    def insert(self, key: int, data):
        """
        Inserta una key en el árbol respetando la estructura.
        """
        if self.is_empty():
            self.root = Node(key, data)
        else:
            self.get_root().insert(key, data)
        
        self.height = self.root.get_height()
        self.size += 1
        
        
    def search_key(self, key) -> Node:
        """
        Busca un key en el árbol y retorna (si existe) el nodo que lo contiene.
        """
        temp: Node = self.get_root()
        
        while temp:
            if temp.get_key() == key:
                return temp
            elif temp.get_key() > key:
                temp = temp.get_left()
            else:
                temp = temp.get_right()
                
        return None
    
    
    def remove_key(self, key):
        """
        Recibe un dato y remueve del árbol el nodo al que le corresponde.
        """
        nodo: Node = self.search_key(key)
        
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
                nodo.key, temp.key = temp.key, nodo.key
                self.remove_key(temp)
            elif nodo.has_right():
                temp: Node = nodo.leftmost_node_of_right_subtree()
                nodo.key, temp.key = temp.key, nodo.key
                self.remove_key(temp)
        
            self.size -= 1
            self.height = self.get_root().get_height()
    
    
    
    def traverse(self, orden: str = "in") -> tuple[str]:
        """
        Retorna tupla con recorrido del árbol en el orden especificado.
        
        orden = "pre" | "in" | "pos" 
        """
        
        root: Node = self.get_root()
        recorrido: list[str] = []
        
        def visit(node: Node): recorrido.append(node.get_key())
        
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
        
        
    def mostrar_arbol(self, nodo: Node, header = "", last = True):
        elbow = "└──"
        pipe = "│  "
        tee = "├──"
        blank = "   "
        print(header + (elbow if last else tee), nodo.get_data())
        if nodo.has_left() and nodo.get_left().get_data() != None:
            self.mostrar_arbol(nodo.get_left(), header = header + (blank if last else pipe), last = False)
        if nodo.has_right() and nodo.get_right().get_data() != None:
            self.mostrar_arbol(nodo.get_right(), header = header + (blank if last else pipe), last = True)
        
    
    #Métodos dunder
    def __str__(self):
        self.mostrar_arbol(self.get_root())
    
    
    def __repr__(self):
        return f"{self.traverse()}"
        
    
if __name__ == "__main__":
    T: Tree = Tree()
    
    T.insert(2,"uno")
    T.insert(1,"dos")
    T.insert(3,"tres")
    T.insert(4,"cuatro")
    T.insert(0,"cinco")
    

    print(T)
    