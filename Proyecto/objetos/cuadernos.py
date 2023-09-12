from dataclasses import dataclass

from objetos.producto import Producto



@dataclass(order=True)
class Cuaderno(Producto):
    _marca: str

    def __post_init__(self):
        super().__post_init__()

    @property
    def marca(self):
        return self._marca
