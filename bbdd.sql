create table soilmoisture (
    id int auto_increment,
    ID_sensor int,
    latitud float,
    longitud float,
    humitat float,
    is_pump boolean,
    ts timestamp,
    primary key(id)
);

create table autobus_parada (
    id int auto_increment,
    ID_parada int unique,
    latitud float,
    longitud float,
    linies text,
    primary key(ID_parada)
);

create table autobus_bus (
    id int auto_increment,
    ID_bus int,
    ID_parada int,
    linia text,
    ts timestamp,
    foreign key(ID_parada) references autobus_parada(ID_parada),
    primary key(id)
);

create table cameres (
    id int auto_increment,
    ID_camera int,
    latitud float,
    longitud float,
    intensitat_transit int,
    accident_flag boolean,
    ts timestamp,
    primary key(id)
);

create table contenidors (
    id int auto_increment,
    ID_contenidor int,
    latitud float,
    longitud float,
    nombre_contenidors int,
    estat_contenidors text,
    ts timestamp,
    primary key(id)
);

create table contaminacio (
    id int auto_increment,
    ID_sensor int,
    latitud float,
    longitud float,
    tipus_sensor int,
    valor float,
    ts timestamp,
    primary key(id)
);

create table bicicleta_stop (
    id int auto_increment,
    ID_parada int,
    latitud float,
    longitud float,
    nombre_llocs int,
    nombre_llocs_ocupats int,
    nombre_llocs_lliures int,
    ts timestamp,
    primary key(id)
);