import os
from tabulate import tabulate
from typing import List, Any, Tuple
from src.clientes import ClienteManager
from src.computadoras import ComputadoraManager
from src.sesiones import SessionManager

cliente_manager = ClienteManager()
computadora_manager = ComputadoraManager()
sesion_manager = SessionManager()

def print_menu() -> int:
    try:
        print("-"*5, "MENU CYBER", "-"*5)
        print("1. Agregar Cliente")
        print("2. Modificar Cliente")
        print("3. Eliminar Cliente")
        print("4. Agregar Computadora")
        print("5. Asignar Computadora")
        print("6. Liberar Computadora")
        print("7. Listar Computadora")
        print("8. Consultar Estado Computadora")
        print("9. Iniciar Sesion")
        print("10. Finalizar Sesion")
        print("11. Mostrar Sesiones")
        print("\n")
        
        print("14. Limpiar Pantalla")
        print("15. Salir")
        
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
        
        elif opcion == 4:
            nombre_computadora: str = input("\tIngrese el nombre de la PC: ")
            
            computadora_manager.agregar_computadora(nombre=nombre_computadora)
            
            print(f"\tSe agregó la computadora: {nombre_computadora}")

        elif opcion == 5:
            try:
                id_computadora: int = int(input("\tIngrese el ID a asignar: "))
            except Exception:
                print("\tID erroneo")
                continue            
            
            computadora_manager.asignar_computadora(computadora_id=id_computadora)
            
        elif opcion == 6:
            try:
                id_computadora: int = int(input("\tIngrese el ID a liberar: "))
            except Exception:
                print("\tID erroneo")
                continue            
            
            computadora_manager.liberar_computadora(computadora_id=id_computadora)
        
        elif opcion == 7:
            lista_computadoras: List[Any] = computadora_manager.listar_computadoras()
            
            lista_computadoras = [(pc.nombre, 'Libre' if pc.estado else 'Ocupada') for pc in lista_computadoras]
            
            print(tabulate(lista_computadoras, ['Nombre PC', 'Estado']))
     
        elif opcion == 8: 
            try:
                id_computadora: int = int(input("\tIngrese el ID a liberar: "))
            except Exception:
                print("\tID erroneo")
                continue 
            
            estado: str = "Libre" if computadora_manager.consultar_estado(computadora_id=id_computadora) else "Ocupada"
            
            print(f"\tLa computadora con ID: {id_computadora} está {estado}") 
            
        elif opcion == 9:
            try:
                id_usuario: int = int(input("\tIngrese el ID Usuario: "))
                id_computadora: int = int(input("\tIngrese el ID Computadora: "))
            except Exception:
                print("\tID erroneo")
                continue 
            
            sesion_manager.iniciar_sesion(cliente_id=id_usuario, computadora_id=id_computadora)
            
            print(f"\tSe inició una nueva sesión.")
            
        elif opcion == 10:
            try:
                id_sesion: int = int(input("\tIngrese el ID: "))
            except Exception:
                print("\tID erroneo")
                continue 
            
            sesion_manager.finalizar_sesion(sesion_id=id_sesion)
            
            print(f"\tSe finalizó la sesión con ID {id_sesion}.")
            
        elif opcion == 11:
            sesiones: List[Tuple[int, float]] = [(s.id, s.costo_total) for s in sesion_manager.mostrar_sesiones()]
        
            print(tabulate(sesiones, ['ID Sesion', 'Costo Total']))
        
        elif opcion == 14:
            os.system('cls')
            
        elif opcion == 15:
            print("Saliendo del programa.")
            exit()