from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# Define la tabla de asociación para User y Rol
rolxusuario = Table('rolxusuario', Base.metadata,
    Column('idusuario', Integer, ForeignKey('usuarios.idusuario')),
    Column('idrol', Integer, ForeignKey('rol.idrol'))
)

# Define la tabla de asociación para User y Carrera
usuarioxcarrera = Table('usuarioxcarrera', Base.metadata,
    Column('idusuario', Integer, ForeignKey('usuarios.idusuario')),
    Column('idcarrera', Integer, ForeignKey('carrera.idcarrera'))
)

# Define la tabla de asociación para User y Atributo
atributosxusuario = Table('atributosxusuario', Base.metadata,
    Column('idusuario', Integer, ForeignKey('usuarios.idusuario')),
    Column('idatributo', Integer, ForeignKey('atributos.idatributo'))
)

class User(Base):
    __tablename__ = "usuarios"

    idusuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    correo = Column(String)
    celular = Column(Integer)
    direccion = Column(String)
    contraseña = Column(String)
    estado = Column(Integer)
    fechacreacion = Column(DateTime)

    # Define la relación con Rol
    roles = relationship("Rol", secondary=rolxusuario, back_populates="users")

    # Define la relación con Carrera
    carreras = relationship("Carrera", secondary=usuarioxcarrera, back_populates="users")

    # Define la relación con Atributo
    atributos = relationship("Atributo", secondary=atributosxusuario, back_populates="users")

    # Define la relación con Aplicante
    aplicantes = relationship("Aplicante", back_populates="user")

class UserIn(BaseModel):
    nombre: str
    apellido: str
    correo: str
    celular: int
    direccion: str
    contraseña: str
    estado: int
    role_ids: [int] = []
    carrera_ids: [int] = []
    atributo_ids: [int] = []
