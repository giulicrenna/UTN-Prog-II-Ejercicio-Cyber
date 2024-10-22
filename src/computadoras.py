from typing import List
from src.db import SessionLocal, Computadora

class ComputadoraManager:
    def __init__(self):
        self.db = SessionLocal()
        
    def listar_computadoras(self) -> List[Computadora]:
        return self.db.query(Computadora).all()
    
    def agregar_computadora(self, *, nombre: str) -> None:
        nueva_computadora: Computadora = Computadora(nombre=nombre)
        
        self.db.add(nueva_computadora)
        self.db.commit()
        self.db.refresh(nueva_computadora)
    
    def asignar_computadora(self, *, computadora_id) -> None:
        computadora: Computadora = self.db.query(Computadora).filter(Computadora.id == computadora_id).first()
        
        if computadora and computadora.estado:
            computadora.estado = False
            
            self.db.commit()
    
    def liberar_computadora(self, *, computadora_id) -> None:
        computadora: Computadora = self.db.query(Computadora).filter(Computadora.id == computadora_id).first()
        
        if computadora and not computadora.estado:
            computadora.estado = True
            
            self.db.commit()
            
    def consultar_estado(self, *, computadora_id) -> str | bool:
        computadora: Computadora = self.db.query(Computadora).filter(Computadora.id == computadora_id).first()
        
        return computadora.estado if computadora else False