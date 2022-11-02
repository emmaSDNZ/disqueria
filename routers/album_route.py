from fastapi import APIRouter
from db.config import mycursor

album = APIRouter()


@album.get('/api/album')
def getAllbum():
     
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
        on album.id_interprete = formato.id_formato;")

    myresult = mycursor.fetchall()
    return myresult


@album.get('/api/album/{id}', )
def getAlbumId( id: str ):

    query = "select cod_album, nombre_album,   \
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
        on album.id_interprete = formato.id_formato \
        where id_album = " 
   
    mycursor.execute( query + id )
    return  mycursor.fetchall()

@album.post('/api/album')
def create_album():
    return {"hola"}