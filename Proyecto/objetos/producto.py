from typing import List
from dataclasses import dataclass, field
from typing import Any, ClassVar

@dataclass(order=True)
class Producto:
    sorted_index: Any = field(init=False, repr=False)
    _impuesto: float
    _lista_productos: ClassVar[List['Producto']] = []
    _codigo: int
    _nombre: str
    _precio: float
    _stock: int

    def __post_init__(self):
        Producto._lista_productos.append(self)
        # hago el calculo del precio con impuesto y se lo seteo al producto cuando lo creo
        self._precio = self._precio + (self._precio * self._impuesto)

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
        self._precio = precio * (1 + self._impuesto)


    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        self._stock = stock


    @classmethod
    def mostrar_productos_ordenados(cls):
        """Ordena los productos de la lista antes de mostrarlos"""
        # Lógica para mostrar productos ordenados por precio
        productos_ordenados = sorted(cls. _lista_productos, key=lambda x: x.precio)
        for producto in productos_ordenados:
            print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}")


    @classmethod
    def buscar_producto(cls, codigo):
        """busca un producto en la lista de por 
        su código y devuelve el producto si lo encuentra, o None si no lo encuentra"""
        for producto in cls._lista_productos:
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
    

