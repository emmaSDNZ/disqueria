
from pydantic import BaseModel
from typing import Optional
from datetime import date

class AlbumSchema(BaseModel):
    #id: Optional[int]
    cod_album: int
    nombre_album: str
    id_interprete: int
    id_genero: int
    cant_temas: int
    id_discografica: int
    id_formato: int
    fec_lanzamiento: date
    precio_album: int
    cantidad_album: int
    caratula_caratula: Optional[str]

