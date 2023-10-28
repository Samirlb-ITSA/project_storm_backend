from pydantic import BaseModel

class Empresa(BaseModel):
    idempresa: int
    nombre: str
    correo: str
    celular: int
    direccion: str
    nit: int