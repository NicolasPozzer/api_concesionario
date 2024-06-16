from pydantic import BaseModel
from typing import Optional

class Vehiculo(BaseModel):
    id: Optional[int] = 999
    marca: str
    modelo: str
    price: float
    velocidad: float