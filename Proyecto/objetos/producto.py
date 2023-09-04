from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Producto:
    sorted_index: Any = field(init=False, repr=False)
    _impuesto: float
    _lista_productos: list = []
    _codigo: int
    _nombre: str
    _precio: float
    _stock: int

    def __post_init__(self):
        self.sorted_index = self._precio
        Producto._lista_productos.append(self)

    @property
    def impuesto(self):
        return self._impuesto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        self._stock = stock
    @classmethod
    def calcular_precio_con_impuesto(cls):
        return cls.precio + (cls.precio * cls.impuesto)

    @classmethod
    def buscar_producto(cls, codigo):
        """busca un producto en la lista de productos de la librería por 
        su código y devuelve el producto si lo encuentra, o None si no lo encuentra"""
        for producto in cls.lista_productos:
            if producto.codigo == codigo:
                return producto
        return None

    @classmethod
    def vender_producto(cls, codigo, cantidad):
        """ busca un producto por su código, verifica si es posible realizar
          la venta en función del stock disponible"""
        producto = cls.buscar_producto(codigo)
        if producto is None:
            print("Producto no encontrado.")
        elif cantidad > producto.stock:
            print("Stock insuficiente para realizar la venta.")
        else:
            producto.stock -= cantidad
            print(f"Venta realizada. Nuevo stock de {producto.nombre}: {producto.stock}")
