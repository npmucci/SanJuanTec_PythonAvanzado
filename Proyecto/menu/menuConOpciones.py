from typing import List
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


