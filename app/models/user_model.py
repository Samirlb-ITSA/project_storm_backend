from pydantic import BaseModel

class User(BaseModel):
    idusuario: int = None
    nombre: str = None
    apellido: str = None
    correo: str = None
    celular: int = None
    direccion: str = None
    contraseña: str = None
    estado: int = None
    fechacreacion:str = None
    