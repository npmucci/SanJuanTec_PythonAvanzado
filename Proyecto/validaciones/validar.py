def cadena_no_vacia(entrada : str) -> bool:
    """Recibe un String y valida si está vacío
       Devuelve True o False y lanza una excepción""" # esta es la forma de documentar lo que hace cada funcion

    if len(entrada)>0:
        return True
    else:
        raise Exception()
    
def opcion_correcta(entrada :int)-> bool:
    """Recibe un String y valida que este entre las opciones del menú
    Devuelve True o False y lanza una excepción"""

    if 1 <= entrada <= 5:
        return True
    else:
        raise Exception()

