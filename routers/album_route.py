from fastapi import APIRouter
from db.config import mycursor, mydb
from schema.album_schema import  AlbumSchema

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
        on album.id_interprete = formato.id_formato \
        where id_album = " 
   
    mycursor.execute( query + id )
    return  mycursor.fetchall()

#Me crea un album
@album.post('/api/album')
def create_Album( album: AlbumSchema ):
    print(album)
    sql = "INSERT INTO album (cod_album, nombre_album, id_interprete, id_genero, cant_temas, id_discografica, id_formato, fec_lanzamiento, precio_album, cantidad_album) \
        VALUES ('" +str(album.cod_album) + "', '"+ album.nombre_album +"', '"+str(album.id_interprete)+ "', '"+str(album.id_genero)+ "' , '" + str(album.cant_temas) + "' , '"+str(album.id_discografica)+ "', '"+str(album.id_formato)+ "', '" +str(album.fec_lanzamiento)+"', '" + str(album.precio_album) +"', '" + str(album.cantidad_album)+ "')"   
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    
    return {"Insert to Album " : album.nombre_album}



""" 
    {
  "cod_album": 12345675,
  "nombre_album": "string",
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