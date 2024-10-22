from typing import Optional, Any
from src.db import SessionLocal, Cliente

"""
Clientes: Registra los datos personales de los clientes.
    ID (Entero, clave primaria)
    Nombre (Cadena de caracteres)
    DNI (Cadena de caracteres única)
    Fecha de registro (Fecha)
Computadoras: Registro de las computadoras disponibles.
    ID (Entero, clave primaria)
    Nombre o número de computadora (Cadena de caracteres)
    Estado (Booleano: Disponible/Ocupada)
Sesiones: Registra el uso de cada computadora por un cliente.
    ID (Entero, clave primaria)
    Cliente ID (Clave foránea de la tabla Clientes)
    Computadora ID (Clave foránea de la tabla Computadoras)
    Hora de inicio (Fecha y hora)
    Hora de fin (Fecha y hora)
    Costo total de la sesión (Flotante, calculado)
"""


class ClienteManager:
    def __init__(self):
        self.db = SessionLocal()
        
    def registrar_cliente(self, *, nombre: str, dni: str) -> Cliente:
        nuevo_cliente: Cliente = Cliente(nombre=nombre, dni=dni)
        self.db.add(nuevo_cliente)
        self.db.commit()
        self.db.refresh(nuevo_cliente)
        
        return nuevo_cliente
    
    def modificar_cliente(self, *, cliente_id: int, nombre: Optional[str] = None,
                          dni: Optional[str] = None) -> None:
        cliente: Any = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        
        if not cliente: return None
        if not nombre: return None
        if not dni: return None
        
        cliente.nombre = nombre
        cliente.dni = dni
        
        self.db.commit()
        
    def eliminar_cliente(self, *, cliente_id: int) -> None:
        cliente: Any = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente: return None
        
        self.db.delete(cliente)
        self.db.commit()
        
    @staticmethod
    def is_valid(*, nombre: str, dni: str) -> bool:
        if nombre == "" or len(nombre.split(" ")) < 2:
            print("\tNombre Incorrecto")
            return False
        
        try:
            if len(dni) > 8:
                print("\tDNI Incorrecto")
                return False
        except TypeError:
            print("\tEl DNI debe ser un numero.")
            return False
        except ValueError:
            print("\tEl DNI debe ser un numero.")
            return False
            
        return True