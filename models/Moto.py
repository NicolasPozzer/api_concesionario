from typing import Optional
from pydantic import BaseModel
from models.Vehiculo import Vehiculo

class Moto(Vehiculo):
    id_moto: Optional[int] = 999
    electrica: bool