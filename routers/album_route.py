from fastapi import APIRouter
from db.config import mycursor

album = APIRouter()

@album.get('/api/album')
def getAllbum():

    mycursor.execute("SELECT * FROM album")
    myresult = mycursor.fetchall()
    return myresult

@album.get('/api/genero')
def getGeneros():
    mycursor.execute("SELECT * FROM genero")
    myresult = mycursor.fetchall()
    return myresult

