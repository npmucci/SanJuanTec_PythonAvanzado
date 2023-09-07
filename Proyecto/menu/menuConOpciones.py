from typing import List
from objetos.cuadernos import Cuaderno
from objetos.libro import Libro
from objetos.producto import Producto
import validaciones as val
def mostrarMenu (titulo : str, opciones: List[str])-> None: # con la flecha y el none le indicamos que la funcion no retorna nada
    opcion = 0
   
    while opcion != 5:
        try:
            print()
            print(titulo)
            print()

            for i, opcion_texto in enumerate(opciones, start=1):
                print(f"{i}. {opcion_texto}")
            entrada = input("Ingrese el número de la opción deseada: ")

            if val.cadena_no_vacia(entrada) and entrada.isdigit():
                opcion = int(entrada)
                if val.opcion_correcta(opcion):
                    if opcion == 5:
                        print("Saliendo del menú.")
                        break
                    else:
                        print("En un momento estaremos procesando su solicitud.")
                      
        except Exception:
            print("Error en la entrada. Intente nuevamente.")

    if opcion == "1":
            codigo = int(input("Ingrese el código del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            impuesto = float(input("Ingrese el impuesto del producto (como decimal, ej. 0.1 para 10%): "))

            tipo_producto = input("Seleccione el tipo de producto (Libro/Cuadernos): ").capitalize()

            if tipo_producto == "Libro":
                autor = input("Ingrese el autor del libro: ")
                producto = Libro(impuesto, codigo, nombre, precio, stock, autor)
            elif tipo_producto == "Lapiz":
                color = input("Ingrese el color del lápiz: ")
                producto = Cuaderno(impuesto, codigo, nombre, precio, stock, color)
            else:
                print("Tipo de producto no válido.")

    elif opcion == "2":
            codigo_buscar = int(input("Ingrese el código del producto a buscar: "))
            producto_encontrado = Producto.buscar_producto(codigo_buscar)
            if producto_encontrado:
                print(f"Producto encontrado: {producto_encontrado.nombre}")
            else:
                print("Producto no encontrado.")

    elif opcion == "3":
            Producto.mostrar_productos_ordenados()

    elif opcion == "4":
            codigo_vender = int(input("Ingrese el código del producto a vender: "))
            cantidad_vender = int(input("Ingrese la cantidad a vender: "))
            Producto.vender_producto(codigo_vender, cantidad_vender)

    elif opcion == "5":
            print("Saliendo del programa.")
    

    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")