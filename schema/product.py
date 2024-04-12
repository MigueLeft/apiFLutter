from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    codigo: Optional[int]
    nombre: str
    descripcion: str
    cantidad: int
    precio: float