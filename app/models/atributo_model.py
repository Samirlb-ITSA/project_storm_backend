from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# Define la tabla de asociación para User y Atributo
atributosxusuario = Table('atributosxusuario', Base.metadata,
    Column('idusuario', Integer, ForeignKey('usuarios.idusuario')),
    Column('idatributo', Integer, ForeignKey('atributos.idatributo'))
)

class Atributo(Base):
    __tablename__ = "atributos"

    idatributo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

    # Define la relación con usuarios
    users = relationship("usuarios", secondary=atributosxusuario, back_populates="atributos")

class AtributoIn(BaseModel):
    idatributo: int
    nombre: str