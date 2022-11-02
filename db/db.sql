create database disqueria;

use disqueria;

create table genero (
    id_genero int not null auto_increment primary key,
    nombre varchar(50)
);

create table discografica(
    id_discografica int not null auto_increment primary key,
    nombre varchar(50)
);

create table formato(
    id_formato int not null auto_increment primary key,
    tipo varchar(50)
);

create table interprete(
    id_interprete int not null auto_increment primary key,
    nombre varchar(50),
    apellido varchar(50),
    nacionalidad varchar(50),
    foto varchar(100)
);

create table album(
    id_album int auto_increment primary key,
    cod_album int not null,
    nombre varchar(100) not null,
    id_interprete int not null,
    id_genero int not null,
    cant_temas int not null,
    id_discografica int not null,
    id_formato int not null,
    fec_lanzamiento date,
    precio real not null,
    cantidad int not null,
    caratula varchar(100),
    foreign key(id_genero) references genero(id_genero),
    foreign key(id_discografica) references discografica(id_discografica),
    foreign key(id_formato) references formato(id_formato)
    ); 

create table tema(
        id_tema int auto_increment primary key,
        titulo varchar(100),
        duracion time,
        autor varchar(100) not null,
        compositor varchar(100) not null,
        id_album int,
        id_interprete int,
        foreign key(id_album) references album(id_album),
        foreign key(id_interprete) references interprete(id_interprete)
    );



    
    use disqueria;
    insert into interprete values (null,'Laura','Pausini','Italia',null);
    insert into interprete values (null,'Raúl','DiBlasio','Argentina',null);
    insert into interprete values (null,'Richard','Clayderman','Francia',null);
    insert into interprete values (null,'Enya','Brennan','Irlanda',null);
    insert into interprete values (null,'Vangelis','Papathanasiouss','Grecia',null);
    insert into interprete values (null,'Jean Michel','Jarre','Francia',null);
    insert into interprete values (null,'La Mona','Gimenez','Argentina',null);
    insert into interprete values (null,'Chaqueño','Palavecino','Argentina',null);
    insert into interprete values (null,'Hermanos','Pimpinela','Argentina',null);
    insert into interprete values (null,'Ulises','Bueno','Argentina',null);
    insert into interprete values (null,'Leo','Mattioli','Argentina',null);
    insert into interprete values (null,'Carlos','Gardel','Argentina',null);
    insert into interprete values (null,'Aztor','Piazzolla','Argentina',null);
    insert into interprete values (null,'Michael','Jackson','USA',null);
    insert into interprete values (null,'Luis Miguel','Gallego Basteri','Mexico',null);
    insert into interprete values (null,'José Luis','Perales','España',null);
    insert into interprete values (null,'Julio','Iglesias','España',null);
    insert into interprete values (null,'Rosana','Arbelo Gopar','España',null);


use disqueria;
insert into discografica values (null,'BMG'),(null,'Sony Music'),(null,'WEA'),(null,'Universal'),(null,'Independiente');

insert into genero values (null,'Pop'),(null,'Tango'),(null,'Bolero'),(null,'Folklore'),(null,'Instrumental'),(null,'Electrónica');


insert into formato values (null,'Compact Disc'),(null,'Cassette'),(null,'Long Play'),(null,'Digital');


insert into album values (null,1234567,'Lêttre à ma Mère',3,5,10,5,3,'1979-01-01',1000,2,null);
insert into album values (null,1234568,'Las Cosas Que Vives',1,1,12,3,1,'1996-01-01',1000,1,null);
insert into album values (null,1234569,'En Tiempo de Amor',2,5,10,1,1,'1993-01-01',1000,1,null);
insert into album values (null,1234570,'El Piano de América',2,5,10,1,1,'1994-01-01',1000,1,null);


insert into tema values (null,'Lêttre à ma Mère','00:40:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,"Mariage D'Amour",'00:03:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,"Souvenirs D'Enfance",'00:03:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,"Nostalgie",'00:03:00','Paul De Senneville','Paul De Senneville',1,3);
