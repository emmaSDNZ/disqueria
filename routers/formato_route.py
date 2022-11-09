from fastapi import APIRouter
from db.config import mycursor, mydb
from schema.formato_schema import FormatoSchema

formato = APIRouter()

@formato.get('/api/formato')


@formato.get('/api/formato')
def get_Formato():
    mycursor.execute("SELECT * FROM formato;")
    myresult = mycursor.fetchall()
    return myresult

@formato.get('/api/formato/{id}')
def get_Formato_ID( id: str ):
    query_Select = "select tipo_formato from formato where id_formato= ' "+ id +"';"
    mycursor.execute(query_Select)  
    id_SEARCH =  mycursor.fetchall()
    if ( id_SEARCH == []):
        return { "mssg" : "ID INVALIDO"} 
    return id_SEARCH

@formato.get('/api/formato/album/{id}')
def get_Formato_Album(id : str):
    query_Select = "SELECT * from formato \
                    INNER JOIN  album ON  \
                    formato.id_formato = album.id_formato \
                    where formato.id_formato="+ id +";"
    mycursor.execute( query_Select )
    result = mycursor.fetchall()
    if( result == [] ):
        return { "msg" : "ID invalido"}
    return result  


@formato.post('/api/formatos')
def create_Formato( formato: FormatoSchema ):
    sql = "INSERT INTO formato (tipo_formato) VALUES ('" + formato.tipo_formato + "');"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    return {"Insert to genere " : formato.tipo_formato }


@formato.put("/API/formato/{id}")
async def update_Formato(id: str , formato : FormatoSchema):
    
    sql = "UPDATE formato SET tipo_formato = ' " + formato.tipo_formato + "' WHERE id_formato = ' "+ id +"'"
    mycursor.execute(sql)
    mydb.commit()  

    query_Select = "select tipo_formato from formato where id_formato= ' "+ id +"'"
    mycursor.execute(query_Select)   
    return mycursor.fetchall()
    

  
@formato.delete('/api/formato/{id}')
def delete_Formato_Id(id):
    sql = "DELETE FROM formato WHERE id_formato = ' "+ id + " '"
    mycursor.execute(sql)
    mydb.commit()

    return { "DELETED" }

