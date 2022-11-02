from fastapi import APIRouter
from db.config import mycursor, mydb
from schema.genero_schema import GeneroSchema

generos = APIRouter()

#Muestra todos los genero
@generos.get('/api/generos')
def getGeneros():
    mycursor.execute("SELECT * FROM genero")
    myresult = mycursor.fetchall()
    return myresult

#Muestra un genero segun su ID
@generos.get('/api/generos/{id}')
def getGeneros( id: str ):
    query_Select = "select nombre_genero from genero where id_genero= ' "+ id +"'"
    mycursor.execute(query_Select)   
    return mycursor.fetchall()
      
#Me crea un genero
@generos.post('/api/generos')
def create_Genero( genero: GeneroSchema ):
    sql = "INSERT INTO genero (nombre_genero) VALUES ('" + genero.nombre_genero + "')"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    return {"Insert to genere " : genero.nombre_genero }

# Modifica un genero segun ID
@generos.put("/API/genero/{id}")
async def update_Genero(id: str , genero : GeneroSchema):
    sql = "UPDATE genero SET nombre_genero = ' " + genero.nombre_genero + "' WHERE id_genero = ' "+ id +"'"
    mycursor.execute(sql)
    mydb.commit()  

    query_Select = "select nombre_genero from genero where id_genero= ' "+ id +"'"
    mycursor.execute(query_Select)   
    return mycursor.fetchall()
    

# Elimina un genero segun ID   
@generos.delete('/api/generos/{id}')
def deleteGeneroId(id):
    sql = "DELETE FROM genero WHERE id_genero = ' "+ id + " '"
    mycursor.execute(sql)
    mydb.commit()

    return {"DELETED"}



