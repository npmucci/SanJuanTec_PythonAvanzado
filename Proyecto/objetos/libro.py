from dataclasses import dataclass

from objetos.producto import Producto



@dataclass (order=True)
class Libro(Producto):
    _Isbn: str
    _autor: str

 
    @property
    def Isbn(self):
        return self._Isbn

    @Isbn.setter
    def Isbn(self, value):
        self._Isbn = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value





