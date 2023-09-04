import dataclasses

from Proyecto.objetos.producto import Producto

@dataclasses(order=True)
class Cuaderno(Producto):
    __marca: str

    def __post_init__(self):
        super().__post_init__()

    @property
    def marca(self):
        return self.__marca

  
    