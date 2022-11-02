from fastapi import APIRouter
from db.config import mycursor

formato = APIRouter()

@formato.get('/api/formato')
def getGeneros():
    return {
        "message" : "ApiRest disqueria",
        "version": "1.0.0",
        "satus": True,
        "route" : "FORMATO"
        }
