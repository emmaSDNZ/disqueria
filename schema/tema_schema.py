from pydantic import BaseModel
from typing import Optional

class TemaSchema(BaseModel):
    #id: Optional[int]
    titulo_tema: str
    duracion_tema: int
    autor_tema: str
    compositor_tema: str
    id_album:int 
    id_interprete: int
  