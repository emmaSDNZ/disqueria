from fastapi import APIRouter
from db.config import mycursor

tema = APIRouter()

@tema.get('/api/temas')
def getGeneros():
    return {
        "message" : "ApiRest disqueria",
        "version": "1.0.0",
        "satus": True,
        "route" : "TEMAs"
        }
