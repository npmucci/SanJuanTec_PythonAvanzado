from objetos.libro import Libro
from objetos.cuadernos import Cuaderno
from objetos.producto import Producto
import validaciones as val

def mostrar_menu():
    while True:
        print("Bienvenido al sistema de gestión de productos:")
        print("1. Mostrar lista de productos ordenados por precio.")
        print("2. Agregar un nuevo libro.")
        print("3. Agregar un nuevo cuaderno.")
        print("4. Buscar un producto")
        print("5. Vender un producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if val.cadena_no_vacia(opcion):
                opcion = int(opcion)
                if val.opcion_correcta(opcion):
                    if opcion == 1:
                        if Producto._lista_productos:
                            Producto.mostrar_productos_ordenados()
                        else:
                            print("No hay productos para mostrar.")

                    elif opcion == 2:
                        # Agregar un nuevo libro
                        impuesto = float(input("Ingrese el impuesto: "))
                        isbn = input("Ingrese el ISBN del libro: ")
                        nombre = input("Ingrese el Titulo del libro")
                        autor = input("Ingrese el autor del libro: ")
                        precio = float(input("Ingrese el precio del libro: "))
                        stock = int(input("Ingrese el stock del libro: "))
                        nuevo_libro = Libro(impuesto, len(Producto._lista_productos) + 1, nombre, precio, stock, isbn, autor)
                        print("Libro agregado con éxito")
                    elif opcion == 3:
                        # Agregar un nuevo cuaderno
                        impuesto = float(input("Ingrese el impuesto: "))
                        nombre = input("Ingrese Nombre de Cuaderno")
                        marca = input("Ingrese la marca: ")
                        precio = float(input("Ingrese el precio del cuaderno: "))
                        stock = int(input("Ingrese el stock del cuaderno: "))
                        nuevo_cuaderno = Cuaderno(impuesto, len(Producto._lista_productos) + 1, nombre, precio, stock, marca)
                        print("Cuaderno agregado con éxito")
                    elif opcion == 4:
                        codigo = int(input("Ingrese el código del producto a buscar: "))
                        productoBuscado = Producto.buscar_producto(codigo)
                        if productoBuscado is None:
                            print("El producto solicitado no se encuentra en nuestra base de datos.")
                        else:
                            print("Producto encontrado:")
                            print(f"Código: {productoBuscado.codigo}, Nombre: {productoBuscado.nombre}, Precio: {productoBuscado.precio}")
                    
                    elif opcion == 5:
                        codigo_vender = int(input("Ingrese el código del producto a vender: "))
                        cantidad_vender = int(input("Ingrese la cantidad a vender: "))
                        Producto.vender_producto(codigo_vender, cantidad_vender)
                    
                    elif opcion == 6:
                        print("Saliendo del programa.")
                        break
                else:
                    print("La opción ingresada no es válida.")
            else:
                print("La opción ingresada no es válida.")
        except Exception:
            print("Por favor ingrese una opcion valida")
