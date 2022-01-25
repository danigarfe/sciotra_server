-- TABLAS DE MEDIDAS --
DROP DATABASE bbdd;
CREATE DATABASE bbdd;
USE bbdd;


-- TAULES DE INFORMACIÓ --

create table autobus_parada_info (
    ID_parada int unique,
    nom text,
    latitud float,
    longitud float,
    linies text,
    primary key(ID_parada)
);

INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (309,'Diagonal - Complex Esportiu Universitari','67 E30 E43 E79 E97 E98 L51 L57 L61 L63 L64 L68 L69 L97 567 e17 e20 hillsa mon_bus',41.383268004,2.107874004);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (107037,'Av. Diagonal - Torre Melina','M14',41.383848703,2.110801136);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (310,'Diagonal - Av Doctor Marañón','7 67 175 E30 E43 E79 E97 E98 L97 N12 e8',41.384222004, 2.111612004);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (3174,'Diagonal - Comple Esportiu Universitari','113 V1',41.384080004,2.111706997);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (3233,'ETS Arquitectura','H6 e22 E30 E43 E97 E98 E79 L97 mon_bus',41.384852780,2.114019444);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (2542,'Zona Universitària - Escola T S Enginyeria','7 67 175 L51 L57 L61 L63 L64 L67 M14 e17 e20 N12 N50',41.385076999,2.115683001);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (3222,'Palau Reial Línies','H6 e2.2 E30 E43 E97 E98 E79 L97',41.385847220,2.117969444);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (2543,'Diagonal - Metro Palau','7 33 67 175 M14 N12',41.385863890,2.118772222);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (3234,'Pl. Pius XII','H6 E30 E43 E97 E98 L79 L97',41.386585999,2.120893994);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (492,'Diagonal - Av Joan XXIII','V5 7 33 63 67 78 175 M14 N12',41.386931999,2.122985004);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (493,'Diagonal - Gran Via Carles III','7 33 63 67 78 N12',41.387616670,2.125686111);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (3223,'Pl Reina Maria Cristina','H6 e2.2 E30 E43 E97 E98 E79 L97 M12',41.387834004,2.125799003);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (108719,'Av. Diagonal - Gran Via Carles III','e17 L51 L57 L61 L63 L64 L68 L69 567 N50 e20 M14',41.387850000,2.126613889);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (491,'Diagonal - Joan Güell','V3 70',41.388025997,2.128121997);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (494,'Diagonal - Gandesa','6 7 33 34 63 67 78 N12',41.388442997,2.128934000);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (3440,'Diagonal - Les Corts','101',41.388829996,2.130462003);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (42,'Diagonal - Illa Diagonal','6 7 33 34 63 67 E30 E79 e8 N12',41.389623003,2.133589995);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (110442,'ILLA DIAGONAL','BCTO',41.389844440,2.134486111);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (373,'Diagonal - Entença','6 7 33 34 63 67 E30 E79 L51 L57 L61 L63 L64 L67 L68 e17 e20 N12',41.390340004,2.136404996);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (822,'Diagonal - Av de Sarrià','V9 6 7 33 34 63 67 N12',41.391332003,2.140310000);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (3802,'Diagonal - Pl Francesc Macià','mon_bus',41.392269440,2.144341667);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (106175,'Av. Diagonal - Pl Francesc Macià','N12 e15.2 X1',41.392500000,2.143341667);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (524,'Diagonal - Ganduxer','6 7 33 34 63 67 N12',41.391650003,2.140022997);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (41,'Diagonal - Doctor Fleming','7 33 63 67 78 N12 E30 E79',41.390710003,2.136322005);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (941,'Av. Diagonal - Doctor Fleming','L51 L57 L61 L64 L68 L69 e8 e17 e20',41.39060556,2.135819444);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (483,'Diagonal - Numància','e17 e20 e8 L51 L57 L61 L63 L64 L68 L69',41.389544440,2.131647222);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (105911,'Av. Diagonal - Pl. Reina Maria Cristina','M12',41.388986110,2.127627778);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (237,'Diagonal - Pl Reina Maria Cristina','V5 7 33 63 67 78 175 L51 L57 L61 L63 L64 L68 L69 L97 M14 E30 E43 E79 E97 E98 e17 e20 567 N12 N50',41.388500000,2.127488889);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (262142,'Av. Diagonal/ C. Dr. Ferran (Maria Cristina)','e8 hiilsa',41.388222000,2.126421000);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (262141,'Av. Diagonal/ C. Dr. Ferran (Maria Cristina)','HISPANO_IGUALADINA e20 mon_bus e15.2 BAIX',41.388110100,2.125982000);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (2992,'Pl Pius XII - Av Pedralbes','113',41.387822220,2.122552778);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (766,'Diagonal - Pl Pius XII','67 175 E30 E43 E79 M14 e15.2 mon_bus N12',41.387269440,2.122669444);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (458,'Pl Pius XI','H6 7 33 L97 E97 E98',41.386991670,2.121577778);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (105349,'Av. Diagonal - Palau Reial de Pedralbes','HISPANO_IGUALADINA E97 E98 L97 N12 hillsa e2.2 BAIX e15.2 mon_bus',41.386055560,2.117880556);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (156794,'Av. Diagonal - Palau Reial de Pedralbes','ESCAPADES_ALSINA_GRAELLS',41.385995000,2.117647000);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (21,'Palau Reial','H6 7 33 67 175 E30 E43 E79 L51 L57 L61 L63 L64 L68 L69 M14 567 e17 e20 113',41.385627780,2.116172222);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (2541,'Diagonal - Metro Zona Universitària','67 E30 E43 E79 E97 E98 L51 L57 L61 L63 L64 L67 L68 L69 L97 567 e15.2 e8 e17 e20 HISPANO_IGUALADA N50',41.384861110,2.113169444);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (547,'Metro Zona Universitària','7',41.384763890,2.111483333);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (548,'Zona Universitària - Facultat Economia i Empresa','V1 33 113 175 N12',41.384722222,2.111036111);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (556,'Zona Universitària','H6',41.384625000,2.110941667);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (108891,'Av. Diagonal - González Tablas','M14',41.384419440,2.110269444);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (250,'Diagonal - Manuel Ballbé','67',41.384080560,2.110077778);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (251,'Diagonal - Parc de Cervantes','67 E30 E43 E79 E97 E98 L51 L57 L61 L63 L64 L68 L69 L97 567 e15.2 e17 e20 mon_bus',41.383652780,2.108388889);
INSERT INTO autobus_parada_info (ID_parada, nom, linies, latitud, longitud) VALUES (262144,'Diagonal - Pl. Pius XII','BCTO',41.387163890,2.123858333);

create table bicicleta_parada_info (
    ID_parada int,
    latitud float,
    longitud float,
    primary key(ID_parada)
);

INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (1,41.39082222,2.136677778);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (2,41.39219444,2.142072222);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (3,41.38783333,2.1258);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (4,41.39226944,2.144341667);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (5,41.38562778,2.116172222);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (6,41.38825556,2.125383333);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (7,41.38863333,2.127791667);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (8,41.38755278,2.123233333);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (9,41.38688611,2.12085);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (10,41.38641389,2.119311111);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (11,41.38471389,2.112633333);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (12,41.38397222,2.109691667);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (13,41.38905,2.130861111);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (14,41.38993889,2.134427778);
INSERT INTO bicicleta_parada_info (ID_parada, latitud, longitud) VALUES (15,41.39152778,2.139508333);

create table contenidors_info (    
    ID_contenidor int,
    latitud float,
    longitud float,
    primary key(ID_contenidor)
);

INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (1,41.38585278,2.11665);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (2,41.38701944,2.120536111);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (3,41.38730278,2.121680556);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (4,41.38787778,2.123855556);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (5,41.38830833,2.125058333);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (6,41.38873056,2.12675);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (7,41.38915278,2.128958333);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (8,41.389775,2.131483333);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (9,41.39008611,2.132591667);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (10,41.39022778,2.133475);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (11,41.39081111,2.135469444);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (12,41.39165556,2.138844444);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (13,41.39199722,2.140177778);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (14,41.39223333,2.141130556);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (15,41.39253333,2.142302778);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (16,41.39286111,2.143569444);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (17,41.38326111,2.108433333);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (18,41.38443056,2.113122222);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (19,41.38489167,2.11495);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (20,41.38525,2.1630556);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (21,41.38543611,2.117013889);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (22,41.38619444,2.119952778);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (23,41.38634444,2.12065);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (24,41.38718333,2.123930556);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (25,41.38726944,2.124275);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (26,41.38851389,2.129102778);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (27,41.38893333,2.130530556);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (28,41.39053333,2.137125);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (29,41.39094444,2.138686111);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (30,41.3912361,2.1399);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (31,41.39198056,2.142858333);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (32,41.39219722,2.143625);
INSERT INTO contenidors_info (ID_contenidor, latitud, longitud) VALUES (33,41.38988333,2.13185);

create table soilmoisture_info (
    ID_sensor int,
    latitud float,
    longitud float,
    primary key(ID_sensor)
);

INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (1,41.38453333,2.112969444);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (2,41.38470556,2.113616667);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (3,41.38485833,2.114233333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (4,41.384975,2.14683333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (5,41.38509444,2.115138889);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (6,41.3852,2.115577778);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (7,41.38530278,2.115961111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (8,41.38539722,2.116358333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (9,41.38560556,2.117175);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (10,41.38568889,2.117505556);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (11,41.38578889,2.117908333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (12,41.38606667,2.117355556);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (13,41.38616667,2.117736111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (14,41.38613889,2.119275);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (15,41.386275,2.119733333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (16,41.38653889,2.119247222);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (17,41.38662222,2.119533333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (18,41.38638333,2.120244444);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (19,41.38650556,2.120686111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (20,41.38683333,2.122022222);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (21,41.38694722,2.122475);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (22,41.387025,2.122791667);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (23,41.38710278,2.123083333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (24,41.38728333,2.123786111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (25,41.38734722,2.124013889);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (26,41.38739167,2.124194444);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (27,41.38741667,2.124308333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (28,41.38745,2.124436111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (29,41.38748611,2.124594444);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (30,41.38753611,2.124791667);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (31,41.38760833,2.125086111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (32,41.38768889,2.125358333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (33,41.38773333,2.125569444);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (34,41.38779444,2.125830556);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (35,41.38810278,2.127722222);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (36,41.38850833,2.128625);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (37,41.38861389,2.129022222);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (38,41.38867778,2.129286111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (39,41.38875833,2.129630556);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (40,41.38882222,2.129852778);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (41,41.38893889,2.130322222);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (42,41.389025,2.130661111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (43,41.389125,2.131086111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (44,41.38967222,2.133244444);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (45,41.38984722,2.133894444);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (46,41.39,2.134472222);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (47,41.39010556,2.134925);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (48,41.39018333,2.135252778);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (49,41.39031389,2.135736111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (50,41.39081389,2.137694444);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (51,41.39088056,2.137972222);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (52,41.39097222,2.138352778);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (53,41.39103611,2.138633333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (54,41.39139444,2.139933333);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (55,41.39148611,2.140316667);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (56,41.39154722,2.140572222);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (57,41.39160556,2.140802778);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (58,41.39168611,2.141111111);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (59,41.39177222,2.14145);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (60,41.39183611,2.141716667);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (61,41.39188333,2.1419);
INSERT INTO soilmoisture_info (ID_sensor, latitud, longitud) VALUES (62,41.39196944,2.142241667);


create table cameres_info (
    ID_camera int,
    latitud float,
    longitud float,    
    primary key(ID_camera)
);

INSERT INTO cameres_info (ID_camera, latitud, longitud) VALUES (1,41.38836667,2.127036111);

create table contaminacio_info (    
    ID_sensor int,
    latitud float,
    longitud float,
    primary key(ID_sensor)
);


INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (1,41.39082222,2.136677778);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (2,41.39219444,2.142072222);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (3,41.38783333,2.1258);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (4,41.39226944,2.144341667);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (5,41.38562778,2.116172222);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (6,41.38825556,2.125383333);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (7,41.38863333,2.127791667);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (8,41.38755278,2.123233333);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (9,41.38688611,2.12085);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (10,41.38641389,2.119311111);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (11,41.38471389,2.112633333);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (12,41.38397222,2.109691667);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (13,41.38905,2.30861111);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (14,41.38993889,2.134427778);
INSERT INTO contaminacio_info (ID_sensor, latitud, longitud) VALUES (15,41.39152778,2.139508333);




-- TAULES DE DADES --

create table autobus_bus (
    id int auto_increment,
    ID_bus int,
    ID_parada int,
    linia text,
    ts timestamp,
    foreign key(ID_parada) references autobus_parada_info(ID_parada),
    primary key(id)
);

create table soilmoisture (
    id int auto_increment,
    ID_sensor int,
    humitat float,
    is_pump boolean,
    ts timestamp,
    primary key(id)
);


create table cameres (
    id int auto_increment,
    ID_camera int,
    intensitat_transit int,
    accident_flag boolean,
    ts timestamp,
    primary key(id)
);

create table contenidors (
    id int auto_increment,
    ID_contenidor int,
    nombre_contenidors int,
    estat_contenidors text,
    ts timestamp,
    primary key(id)
);

create table contaminacio (
    id int auto_increment,
    ID_sensor int,
    tipus_sensor int,
    valor float,
    ts timestamp,
    primary key(id)
);

create table bicicleta_stop (
    id int auto_increment,
    ID_parada int,
    nombre_llocs int,
    nombre_llocs_ocupats int,
    nombre_llocs_lliures int,
    ts timestamp,
    primary key(id)
);

create table linies_info (
    ID_linia int unique,
    nom text,
    parades text,
    primary key(ID_linia)
);

INSERT INTO linies_info (ID_linia, nom, parades) VALUES (0,'6', '494,42,373,822,524');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (1,'7', '310,2542,2543,492,493,494,42,373,822,524,41,237,458,21,547');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (2,'33', '2543,492,493,494,42,373,822,524,41,237,458,21,548');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (3,'34', '494,42,373,822,524');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (4,'63', '492,493,494,42,373,822,524,41,237');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (5,'67', '309,310,2542,2543,492,493,494,42,373,822,524,41,237,766,21,2541,250,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (6,'70', '491');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (7,'78', '492,493,494,41,237');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (8,'101', '3440');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (9,'113', '3174,2992,21,548');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (10,'175', '310,2542,2543,492,237,766,21,548');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (11,'E30', '309,310,3233,3222,3234,3223,42,373,41,237,766,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (12,'E79', '309,310,3233,3222,3223,42,373,41,237,766,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (13,'E97', '309,310,3233,3222,3234,3223,237,458,105349,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (14,'E98', '309,310,3233,3222,3234,3223,237,458,105349,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (15,'H6', '3233,3222,3234,3223,458,21,556');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (16,'L51', '309,2542,108719,373,941,483,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (17,'L57', '309,2542,108719,373,941,483,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (18,'L61', '309,2542,108719,373,941,483,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (19,'L63', '309,2542,108719,373,483,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (20,'L64', '309,2542,108719,373,941,483,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (21,'L68', '309,108719,373,941,483,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (22,'L69', '309,108719,941,483,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (23,'L97', '309,310,3233,3222,3234,3223,237,458,105349,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (24,'567', '309,108719,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (25,'e2.2', '3222,3223,105349');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (26,'e8', '310,42,941,483,262142,2541');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (27,'e15.2', '106175,262141,766,105349,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (28,'e17', '309,2542,108719,373,941,483,237,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (29,'e20', '309,2542,108719,373,941,483,237,262141,21,2541,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (30,'e22', '3233');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (31,'hillsa', '309,105349');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (32,'mon_bus', '309,3233,3802,262141,766,105349,251');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (33,'M12', '3223,105911');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (34,'M14', '107037,2542,2543,492,108719,237,766,21,108891');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (35,'N12', '310,2542,2543,492,493,494,42,373,822,106175,524,41,237,766,105349,548');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (36,'N50', '2542,108719,237,2541');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (37,'X1', '106175');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (38,'V1', '3174,548');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (39,'V3', '491');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (40,'V5', '492,237');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (41,'V9', '822');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (42,'BCTO', '110442,262144');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (43,'BAIX', '262141,105349');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (44,'HISPANO_IGUALADINA', '262141,105349,2541');
INSERT INTO linies_info (ID_linia, nom, parades) VALUES (45,'ESCAPADES_ALSINA_GRAELLS', '156794');





















