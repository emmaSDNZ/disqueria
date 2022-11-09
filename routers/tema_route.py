from fastapi import APIRouter
from db.config import mycursor, mydb
from schema.tema_schema import TemaSchema

tema = APIRouter()

#Muestra todos los temas y hace la busqueda
@tema.get('/api/temas')
def get_Temas(params = ""):
    print(len(params))

    if(len(params) == 0):
        mycursor.execute("SELECT * FROM tema;")
        myresult = mycursor.fetchall()
        return myresult
    mycursor.execute("select * from tema WHERE titulo_tema LIKE '% "+params+"%'")
    myresult = mycursor.fetchall()
    return myresult

#Muestra un tema segun su ID
@tema.get('/api/temas/{id}')
def get_Genero_ID( id: str ):
    query_Select = "select titulo_tema from tema where id_tema= ' "+ id +"';"
    mycursor.execute(query_Select)  
    id_SEARCH =  mycursor.fetchall()
    if ( id_SEARCH == []):
        return { "mssg" : "ID INVALIDO"} 
    return id_SEARCH

@tema.get('/api/temas/album/{id}')
def get_Interprete_Album(id : str):
    query_Select = "SELECT id_tema, titulo_tema, duracion_tema, autor_tema, compositor_tema, nombre_album, cod_album, nombre_interprete, apellido_interprete, \
                    nacionalidad_interprete from tema \
                    INNER JOIN  album ON  tema.id_album = album.id_album\
                    INNER JOIN interprete ON tema.id_interprete = interprete.id_interprete\
                    where tema.id_tema="+ id +";"
    mycursor.execute( query_Select )
    result = mycursor.fetchall()
    if( result == [] ):
        return { "msg" : "ID invalido"}
    return result  

#Me crea un tema
@tema.post('/api/temas')
def create_Tema( tema: TemaSchema ):
    sql = "INSERT INTO tema (titulo_tema, duracion_tema, autor_tema, compositor_tema, id_album, id_interprete ) VALUES('"+ tema.titulo_tema + "', '"+ str(tema.duracion_tema )+ "', '"+ tema.autor_tema +"', '"+ tema.compositor_tema +"' , '"+str( tema.id_album)+"', '"+ str(tema.id_album)+"' );"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    return {"Insert to genere " : tema.titulo_tema }

#edita un tema
@tema.put("/API/temas/{id}")
async def update_Tema(id: str , tema : TemaSchema):
    
    sql = "UPDATE tema SET titulo_tema = '"+ tema.titulo_tema +"', duracion_tema = '"+ str(tema.duracion_tema) +"',autor_tema = '"+ tema.autor_tema +"',compositor_tema = '"+ tema.compositor_tema +"', id_album= '"+str(tema.id_album)+"', id_interprete='"+str(tema.id_interprete)+"' WHERE id_tema = ' "+ id +"'"
    mycursor.execute(sql)
    mydb.commit()  

    query_Select = "select titulo_tema from tema where id_tema= ' "+ id +"'"
    mycursor.execute(query_Select)   
    return mycursor.fetchall()
    

  
@tema.delete('/api/tema/{id}')
def delete_Tema_Id(id):
    sql = "DELETE FROM tema WHERE id_tema = ' "+ id + " '"
    mycursor.execute(sql)
    mydb.commit()

    return { "DELETED" }


