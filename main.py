from fastapi import FastAPI
from routers.album_route import album
from routers.genero_route import generos
from routers.discografica_route import discografica
from routers.formato_route import formato
from routers.interprete_route import interprete
from routers.tema_route import tema

app = FastAPI()

@app.get('/')
def root():
    return {
        "message" : "ApiRest disqueria",
        "version": "1.0.0",
        "satus": True,
        }

app.include_router(album)
app.include_router(generos)
app.include_router(discografica)
app.include_router(formato)
app.include_router(interprete)
app.include_router(tema)