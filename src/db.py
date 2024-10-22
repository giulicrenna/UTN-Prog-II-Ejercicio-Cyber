from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    Float,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

engine = create_engine(url="sqlite:///data/cybercafe.db")
SessionLocal = sessionmaker(bind=engine)

# Creacion de las tablas
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, index=False)
    nombre = Column(String, nullable=False)
    dni = Column(String, unique=True, nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now)
    
class Computadora(Base):
    __tablename__ = 'computadoras'
    id = Column(Integer, primary_key=True, index=False)
    nombre = Column(String, nullable=False)
    estado = Column(Boolean, default=True)

class Sesion(Base):
    __tablename__ = 'sesiones'
    id = Column(Integer, primary_key=True, index=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    Computadora_id = Column(Integer, ForeignKey('computadoras.id'), nullable=False)
    hora_inicio = Column(DateTime, default=datetime.now, nullable=False)
    hora_fin = Column(DateTime, nullable=False)
    costo_total = Column(Float, nullable=False)
    
    cliente = relationship('Cliente')
    computadora = relationship('Computadora')

Base.metadata.create_all(bind=engine)    