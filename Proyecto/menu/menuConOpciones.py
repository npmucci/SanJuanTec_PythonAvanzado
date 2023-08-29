from typing import List
from validaciones.validar import cadena_no_vacia
from validaciones.validar import opcion_correcta
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

            if cadena_no_vacia(entrada) and entrada.isdigit():
                opcion = int(entrada)
                if opcion_correcta(opcion):
                    if opcion == 5:
                        print("Saliendo del menú.")
                        break
                    else:
                        print("En un momento estaremos procesando su solicitud.")
        except Exception:
            print("Error en la entrada. Intente nuevamente.")


