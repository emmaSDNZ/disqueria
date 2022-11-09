from fastapi import APIRouter
from db.config import mycursor, mydb
from schema.album_schema import  AlbumSchema

album = APIRouter()

# Todos los album
@album.get('/api/album')
def get_All_Album( param = "id_album", order = "ASC"  ):
    
    mycursor.execute(
        "select id_album, cod_album, nombre_album,   \
        nombre_interprete, apellido_interprete, nacionalidad_interprete, \
        foto_interprete, nombre_genero, caratula_caratula \
        cant_temas, nombre_discografia, tipo_formato, \
        fec_lanzamiento, precio_album, cantidad_album \
        from album \
        inner join interprete \
        on album.id_interprete = interprete.id_interprete \
        inner join genero \
        on album.id_genero = genero.id_genero \
        inner join discografica \
        on album.id_discografica = discografica.id_discografica \
        inner join formato \
        on album.id_formato = formato.id_formato \
        ORDER BY " + param + " " + order +";")

    myresult = mycursor.fetchall()
    return myresult
#busqueda de album dinamica
@album.get('/api/album/search')
def get_Album_search( params, search ):
    print (search)
    mycursor.execute(
        "select id_album, cod_album, nombre_album,   \
        nombre_interprete, apellido_interprete, nacionalidad_interprete, \
        foto_interprete, nombre_genero, caratula_caratula \
        cant_temas, nombre_discografia, tipo_formato, \
        fec_lanzamiento, precio_album, cantidad_album \
        from album \
        inner join interprete \
        on album.id_interprete = interprete.id_interprete \
        inner join genero \
        on album.id_genero = genero.id_genero \
        inner join discografica \
        on album.id_discografica = discografica.id_discografica \
        inner join formato \
        on album.id_formato = formato.id_formato  \
        WHERE "+ str(params) +" LIKE '%"+ str(search) +"%' ;")

    myresult = mycursor.fetchall()
    return myresult    
 
@album.get('/api/album/{id}', )
def get_Album_Id( id: str ):
    searchId = "SELECT id_album from album WHERE id_album = " + id +" ;"
    mycursor.execute(searchId)
    id_SEARCH = mycursor.fetchall()
    if ( id_SEARCH == []):
        return { "mssg" : "ID INVALIDO"}


    query = "select id_album cod_album, nombre_album,   \
        nombre_interprete, apellido_interprete, nacionalidad_interprete, \
        foto_interprete, nombre_genero, caratula_caratula \
        cant_temas, nombre_discografia, tipo_formato, \
        fec_lanzamiento, precio_album, cantidad_album \
        from album \
        inner join interprete \
        on album.id_interprete = interprete.id_interprete \
        inner join genero \
        on album.id_genero = genero.id_genero \
        inner join discografica \
        on album.id_discografica = discografica.id_discografica \
        inner join formato \
        on album.id_formato = formato.id_formato \
        where id_album = " 
   
    mycursor.execute( query + id )
    return  mycursor.fetchall()

# Me crea un album
@album.post('/api/album')
def create_Album( album: AlbumSchema ):
    print(album)
    sql = "INSERT INTO album (cod_album, nombre_album, id_interprete, id_genero, cant_temas, id_discografica, id_formato, fec_lanzamiento, precio_album, cantidad_album) \
        VALUES ('" +str(album.cod_album) + "', '"+ album.nombre_album +"', '"+str(album.id_interprete)+ "', '"+str(album.id_genero)+ "' , '" + str(album.cant_temas) + "' , '"+str(album.id_discografica)+ "', '"+str(album.id_formato)+ "', '" +str(album.fec_lanzamiento)+"', '" + str(album.precio_album) +"', '" + str(album.cantidad_album)+ "')"   
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    
    return {"Insert to Album " : album.nombre_album}


# Modifica un album segun ID
@album.put("/API/album/{id}")
async def update_ALBUM_Id(id: str , album : AlbumSchema):
    searchId = "SELECT id_album from album WHERE id_album = " + id +" ;"
    mycursor.execute(searchId)
    id_SEARCH = mycursor.fetchall()
    if ( id_SEARCH == [] ):
        return { "mssg" : "ID INVALIDO"}

    
    sql = "UPDATE album  JOIN interprete ON album.id_interprete = interprete.id_interprete JOIN genero ON album.id_genero = genero.id_genero \
        JOIN discografica ON album.id_discografica = discografica.id_discografica  JOIN formato ON album.id_formato = formato.id_formato \
        SET album.cod_album = " +str(album.cod_album) + ", album.nombre_album='"+ album.nombre_album +"', \
        album.id_interprete ="+str(album.id_interprete)+ ", album.id_genero="+str(album.id_genero)+ ", \
        album.cant_temas=" + str(album.cant_temas) + ", album.id_discografica ="+str(album.id_formato)+ ", \
        album.id_formato = "+str(album.id_formato)+ ", album.fec_lanzamiento= '" +str(album.fec_lanzamiento)+"', \
        album.precio_album = " + str(album.precio_album) +", album.cantidad_album = " + str(album.cantidad_album)+ " \
        WHERE album.id_album= "+id+" ; "

    
    mycursor.execute(sql)
    mydb.commit()  

     
    return { "UPDATE "}
    
# Elimina un album segun ID   
@album.delete('/api/album/{id}')
def delete_ALBUM_Id(id):
    searchId = "SELECT id_album from album WHERE id_album = " + id +" ;"
    mycursor.execute(searchId)
    id_SEARCH = mycursor.fetchall()
    if ( id_SEARCH == []):
        return { "mssg" : "ID INVALIDO"}

    sql = "DELETE FROM album WHERE id_album = " + str(id)
    mycursor.execute(sql)
    mydb.commit()

    return { "DELETED" }



"""

    {
  "cod_album": 123455,
  "nombre_album": "Python Api",
  "id_interprete": 3,
  "id_genero": 5,
  "cant_temas": 10,
  "id_discografica": 5,
  "id_formato": 3,
  "fec_lanzamiento": "2022-11-03",
  "precio_album": 100005,
  "cantidad_album": 2
  }

 """