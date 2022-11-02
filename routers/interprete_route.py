from fastapi import APIRouter
from db.config import mycursor

interprete = APIRouter()

@interprete.get('/api/interprete')
def getGeneros():
    return {
        "message" : "ApiRest disqueria",
        "version": "1.0.0",
        "satus": True,
        "route" : "INTERPRETE"
        }
