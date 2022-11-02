from fastapi import APIRouter
from db.config import mycursor

discografica = APIRouter()


@discografica.get('/api/discografica')
def getGeneros():
    return {
        "message" : "ApiRest disqueria",
        "version": "1.0.0",
        "satus": True,
        "route" : "DISCOGRAFICA"
        }
