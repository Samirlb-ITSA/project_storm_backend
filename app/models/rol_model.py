from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# Define la tabla de asociación para User y Rol
rolxusuario = Table('rolxusuario', Base.metadata,
    Column('idusuario', Integer, ForeignKey('usuarios.idusuario')),
    Column('idrol', Integer, ForeignKey('rol.idrol'))
)

class Rol(Base):
    __tablename__ = "rol"

    idrol = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

    # Define la relación con User
    users = relationship("User", secondary=rolxusuario, back_populates="roles")

class RolIn(BaseModel):
    idrol: int
    nombre: str