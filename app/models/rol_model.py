from pydantic import BaseModel

class Rol(BaseModel):
    idrol: int
    nombre: str
