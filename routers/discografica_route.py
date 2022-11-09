from fastapi import APIRouter
from db.config import mycursor, mydb
from schema.discografica_schema import DiscograficaSchema

discografica = APIRouter()


#Muestra todos los genero
@discografica.get('/api/discografica')
def get_Discografica():
    mycursor.execute("SELECT * FROM discografica;")
    myresult = mycursor.fetchall()
    return myresult

#Muestra un genero segun su ID
@discografica.get('/api/discografica/{id}')
def get_Discografica_ID( id: str ):
    query_Select = "select nombre_discografia from discografica where id_discografica= ' "+ id +"';"
    mycursor.execute(query_Select)  
    id_SEARCH =  mycursor.fetchall()
    if ( id_SEARCH == []):
        return { "mssg" : "ID INVALIDO"} 
    return id_SEARCH

@discografica.get('/api/discografica/album/{id}')
def get_Discografica_Album(id : str):
    query_Select = "SELECT * from discografica \
                    INNER JOIN  album ON  \
                    discografica.id_discografica = album.id_discografica \
                    where discografica.id_discografica="+ id +";"
    mycursor.execute( query_Select )
    result = mycursor.fetchall()
    if( result == [] ):
        return { "msg" : "ID invalido"}
    return result  

#Me crea un genero
@discografica.post('/api/discografica')
def create_Discografica( discografica: DiscograficaSchema ):
    sql = "INSERT INTO discografica (nombre_discografia) VALUES ('" + discografica.nombre_discografia + "');"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    return {"Insert to genere " : discografica.nombre_discografia }

# Modifica un genero segun ID
@discografica.put("/api/discografica/{id}")
async def update_Discografica(id: str , discografica: DiscograficaSchema ):
    
    sql = "UPDATE discografica SET nombre_discografia = ' " + discografica.nombre_discografia + "' WHERE id_discografica = ' "+ id +"'"
    mycursor.execute(sql)
    mydb.commit()  

    query_Select = "select nombre_discografia from discografica where id_discografica= ' "+ id +"'"
    mycursor.execute(query_Select)   
    return mycursor.fetchall()
    

# Elimina un genero segun ID   
@discografica.delete('/api/discografica/{id}')
def delete_Discografica_Id(id):
    sql = "DELETE FROM discografica WHERE id_discografica = ' "+ id + " '"
    mycursor.execute(sql)
    mydb.commit()

    return { "DELETED" }



