from datetime import datetime
from typing import List
from src.db import Sesion, SessionLocal

class SessionManager:
    def __init__(self):
        self.db = SessionLocal()
        self.tarifa_por_hora: float = 1500.50
        
    def iniciar_sesion(self, *, cliente_id: int, computadora_id: int) -> Sesion:
        nueva_sesion: Sesion = Sesion(cliente_id=cliente_id, computadora_id=computadora_id)
        
        self.db.add(nueva_sesion)
        self.db.commit()
        self.db.refresh(nueva_sesion)
        
        return nueva_sesion
    
    def finalizar_sesion(self, *, sesion_id: int) -> None:
        sesion = self.db.query(Sesion).filter(Sesion.id == sesion_id).first()
        
        if not sesion: return None
        
        sesion.hora_fin = datetime.now()
        sesion.costo_total = self.calcular_costo_total(hora_inicio=sesion.hora_inicio, hora_fin=sesion.hora_fin)
        self.db.commit()
        
    def mostrar_sesiones(self) -> List[Sesion]:
        return self.db.query(Sesion).all()
        
    def calcular_costo_total(self, *, hora_inicio: datetime, hora_fin: datetime) -> float:
        duracion: float = (hora_fin - hora_inicio).total_seconds() / 3600
        
        return round(duracion * self.tarifa_por_hora, 3)