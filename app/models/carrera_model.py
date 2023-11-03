from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# Define la tabla de asociación para User y Carrera
usuarioxcarrera = Table('usuarioxcarrera', Base.metadata,
    Column('idusuario', Integer, ForeignKey('usuarios.idusuario')),
    Column('idcarrera', Integer, ForeignKey('carrera.idcarrera'))
)

class Carrera(Base):
    __tablename__ = "carrera"

    idcarrera = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

    # Define la relación con User
    users = relationship("User", secondary=usuarioxcarrera, back_populates="carreras")

class CarreraIn(BaseModel):
    idcarrera: int
    nombre: str