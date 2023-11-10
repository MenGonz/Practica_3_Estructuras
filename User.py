
class User():
    nombre: str
    identificacion: int
    
    def __init__(self, nombre: str, identificacion: int):
        self.nombre = nombre
        self.identificacion = identificacion
        
    def get_id(self) -> int:
        return self.identificacion

    def get_key(self) -> int:
        return sum(list(map(int,list(str(self.identificacion)))))
    
    