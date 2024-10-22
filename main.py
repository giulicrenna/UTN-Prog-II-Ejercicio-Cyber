from src.clientes import ClienteManager

cliente_manager = ClienteManager()

def print_menu() -> int:
    try:
        print("-"*5, "MENU CYBER", "-"*5)
        print("1. Agregar Cliente")
        print("2. Modificar Cliente")
        print("3. Eliminar Cliente")
        
        print("10. Salir")
        
        return int(input("> "))
    except KeyboardInterrupt:
        print("Se cerró el programa.")
        exit()

if __name__ == '__main__':
    while True:
        opcion: int = print_menu()
        
        if opcion == 1:
            nombre: str = input("\tIngrese un nombre y apellido: ")
            dni: str = input("\tIngrese un DNI: ")
            
            if not cliente_manager.is_valid(nombre=nombre, dni=dni):
                continue
            
            cliente_manager.registrar_cliente(nombre=nombre, dni=dni)
            
            print(f"\tSe creó el cliente: {nombre}")
        
        if opcion == 2:
            try:
                id_cliente: int = int(input("\tIngrese el ID a modificar: "))
            except Exception:
                print("\tID erroneo")
                continue
                
            nombre: str = input("\tIngrese un nuevo nombre y apellido: ")
            dni: str = input("\tIngrese un nuevo DNI: ")
            
            if not cliente_manager.is_valid(nombre=nombre, dni=dni):
                continue
            
            cliente_manager.modificar_cliente(cliente_id=id_cliente,
                                              nombre=nombre,
                                              dni=dni)
            
            print(f"\tSe modificó correctamente el usuario con ID: {id_cliente}")
            
        elif opcion == 3: 
            try:
                id_cliente: int = int(input("\tIngrese el ID a eliminar: "))
            except Exception:
                print("\tID erroneo")
                continue
            
            cliente_manager.eliminar_cliente(cliente_id=id_cliente)
            print(f"\tSe eliminó el cliente con ID: {id_cliente}")
        
        elif opcion == 10:
            print("Saliendo del programa.")
            exit()