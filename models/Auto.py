from typing import Optional
from pydantic import BaseModel
from models.Vehiculo import Vehiculo

class Auto(BaseModel, Vehiculo):
    id_auto: Optional[int] = 999
    puertas: int