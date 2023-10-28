from pydantic import BaseModel

class Aplicante(BaseModel):
    idaplicante: int
    idoferta: int
    idusuario: int
