
class User():
    nombre: str
    identificacion: int
    
    def __init__(self, nombre: str, identificacion: int):
        self.nombre = nombre
        self.identificacion = identificacion
        
    def get_id(self) -> int:
        return self.identificacion

    def get_nombre(self) -> str:
        return self.nombre
    
    def get_key(self) -> int:
        return sum(list(map(int,list(str(self.identificacion)))))
    
    def __str__(self):
        return f"({self.get_nombre()}, {self.get_id()})"
    
    