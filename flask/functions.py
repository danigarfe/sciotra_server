from classes import *

#OBTÉ LA DARRERA ENTRADA DE LA BASE DE DADES DE LA TAULA ESPECIFICADA
#Lo mejor seria coger los últimos 5 buses que han llegado a esa parada especifica a través del timestamp
#autobus_bus es un registro del bus que ha pasado por la parada con ID_parada.
#La clave seria buscar por la ID_Parada y por el últimos timestamp de todas las lineas.
def getlast(table, mysql):
    q = "SELECT * FROM " + table + " ORDER BY id DESC LIMIT 1;"
    cur = mysql.connection.cursor()
    cur.execute(q)
    result = cur.fetchall()
    mysql.connection.commit()
    return result

#INSEREIX A LA TAULA ESPECIFICADA ELS VALORS ESPECIFICATS (values HA DE SER UN VECTOR AMB ELS VALORS EN ORDRE)
def insert(table, values, mysql):
    q = "INSERT INTO " + table + " VALUES("
    for i in range(len(values)-1):
        q = q + str(values[i]) + ','
    q = q + str(values[len(values)-1]) + ');'
    cur = mysql.connection.cursor()
    cur.execute(q)
    result = cur.fetchall()
    mysql.connection.commit()
    return result

# LA IDEA ÉS FER UN THREAD PER A CADA "SENSOR VIRTUAL". COMPORTAMENT DE CADA TIPUS DE SENSOR DEFINIT A classes.py
def initsensors(mysql):
    #hacer array de buses bus[i], recorrer un array de lineas de bus ('L69', 'L70'...) Runearlos TODOS de una.
    #El 0 representa el id_bus. Tiene que ser valor único.
    #autobus_bus(N, id_bus, lin, parades)
    bus = autobus_bus(30, 0, 'L69', [32, 30, 2, 33, 5, 6, 7, 9, 13, 11, 15, 17, 18, 19, 21, 22, 26, 28, 27, 25, 24, 23, 20, 16, 14, 12, 10, 8, 4, 3, 1, 31, 29])
    t = Thread(target=bus.run)
    t.start()
    
    sensor_humitat = soilmoisture(100, 12, 46.52, 47.23)
    t1 = Thread(target=sensor_humitat.run)
    t1.start()
    return 0
