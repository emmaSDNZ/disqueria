from fastapi import APIRouter
from db.config import mycursor, mydb
from schema.genero_schema import GeneroSchema

generos = APIRouter()

#Muestra todos los genero
@generos.get('/api/generos')
def get_Generos():
    mycursor.execute("SELECT * FROM genero;")
    myresult = mycursor.fetchall()
    return myresult

#Muestra un genero segun su ID
@generos.get('/api/generos/{id}')
def get_Genero_ID( id: str ):
    query_Select = "select nombre_genero from genero where id_genero= ' "+ id +"';"
    mycursor.execute(query_Select)  
    id_SEARCH =  mycursor.fetchall()
    if ( id_SEARCH == []):
        return { "mssg" : "ID INVALIDO"} 
    return id_SEARCH

@generos.get('/api/generos/album/{id}')
def get_Generos_Album(id : str):
    query_Select = "SELECT * from genero \
                    INNER JOIN  album ON  \
                    genero.id_genero = album.id_genero \
                    where genero.id_genero="+ id +";"
    mycursor.execute( query_Select )
    result = mycursor.fetchall()
    if( result == [] ):
        return { "msg" : "ID invalido"}
    return result  

#Me crea un genero
@generos.post('/api/generos')
def create_Genero( genero: GeneroSchema ):
    sql = "INSERT INTO genero (nombre_genero) VALUES ('" + genero.nombre_genero + "');"
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
def delete_Genero_Id(id):
    sql = "DELETE FROM genero WHERE id_genero = ' "+ id + " '"
    mycursor.execute(sql)
    mydb.commit()

    return { "DELETED" }



