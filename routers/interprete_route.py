from fastapi import APIRouter
from db.config import mycursor, mydb
from schema.interprete_schema import InterpreteSchema

interprete = APIRouter()



@interprete.get('/api/interpretes')
def get_Interprete():
    mycursor.execute("SELECT * FROM interprete;")
    myresult = mycursor.fetchall()
    return myresult

@interprete.get('/api/interpretes/{id}')
def get_Interpretes_ID( id: str ):
    query_Select = "select nombre_interprete from interprete where id_interprete= ' "+ id +"';"
    mycursor.execute(query_Select)  
    id_SEARCH =  mycursor.fetchall()
    if ( id_SEARCH == []):
        return { "mssg" : "ID INVALIDO"} 
    return id_SEARCH

@interprete.get('/api/interpretes/album/{id}')
def get_Interprete_Album(id : str):
    query_Select = "SELECT  nombre_interprete, apellido_interprete, nacionalidad_interprete, cod_album, nombre_album, nombre_interprete\
                    nombre_genero, tipo_formato, fec_lanzamiento, precio_album, cantidad_album from album \
                    JOIN  interprete ON  album.id_interprete = interprete.id_interprete \
                    JOIN genero ON album.id_genero = genero.id_genero \
                    JOIN discografica ON album.id_discografica = discografica.id_discografica\
                    JOIN formato ON album.id_formato = formato.id_formato \
                    where interprete.id_interprete="+ id +";"
    mycursor.execute( query_Select )
    result = mycursor.fetchall()
    if( result == [] ):
        return { "msg" : "ID invalido"}
    return result  



@interprete.post('/api/interpretes')
def create_Interprete( interprete: InterpreteSchema ):
    sql = "INSERT INTO interprete (nombre_interprete, apellido_interprete, nacionalidad_interprete)  VALUES('"+ interprete.nombre_interprete + "', '"+ interprete.apellido_interprete + "', '"+ interprete.nacionalidad_interprete +"');"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    return {"Insert to genere " : interprete.nombre_interprete }


@interprete.put("/API/interpretes/{id}")
async def update_Interprete(id: str , interprete : InterpreteSchema ):
    
    sql = "UPDATE interprete SET nombre_interprete = ' " + interprete.nombre_interprete + "', apellido_interprete = ' " + interprete.apellido_interprete + "', nacionalidad_interprete = ' " + interprete.nacionalidad_interprete + "' WHERE id_interprete = ' "+ id +"'"
    mycursor.execute(sql)
    mydb.commit()  

    query_Select = "select nombre_interprete from interprete where id_interprete= ' "+ id +"'"
    mycursor.execute(query_Select)   
    return mycursor.fetchall()

   
@interprete.delete('/api/interprete/{id}')
def delete_Interprete_Id(id):
    sql = "DELETE FROM interprete WHERE id_interprete = ' "+ id + " '"
    mycursor.execute(sql)
    mydb.commit()

    return { "DELETED" }



