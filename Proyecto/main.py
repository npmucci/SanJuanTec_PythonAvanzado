import menu.menuConOpciones as menu #le damos un alias al paquete importado para usarlo en el programa
def main():
    menu.mostrarMenu ("Libreria", ["Ingresar Producto", "Buscar Producto", "Listar Productos", "Venta", "Salir"])
  
if __name__ =="__main__":
    main()