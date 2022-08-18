
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    #operador <
    def __lt__(self, __otroObj: object) -> bool:
        if self.nombre < __otroObj.nombre:
            if self.edad < __otroObj.edad:
                return True
        return False
    
    #operador <=
    def __lq__(self, __otroObj: object) -> bool:
        if self.nombre <= __otroObj.nombre:
            if self.edad <= __otroObj.edad:
                return True
        return False