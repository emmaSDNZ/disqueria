
from pydantic import BaseModel
from typing import Optional

class   InterpreteSchema(BaseModel):
    #id: Optional[int]
    nombre_interprete: str
    apellido_interprete: str
    nacionalidad_interprete: str
  