from classes import *
from flask import jsonify
import globals


# FAAAALTAAA--->En la función getLastValueLinia, falta definir en la consulta la parada desde la que se hace esta query
def getLastValueLinia(table, linia):
    q = "SELECT * FROM " + table + " WHERE linia = " + linia + " ORDER BY id DESC LIMIT 1;"
    cur = globals.mysql.connection.cursor()
    cur.execute(q)
    result = cur.fetchall()
    cur.close()
    globals.mysql.connection.commit()
    return result

#OBTÉ LA DARRERA ENTRADA DE LA BASE DE DADES DE LA TAULA ESPECIFICADA
#Lo mejor seria coger los últimos 5 buses que han llegado a esa parada especifica a través del timestamp
#autobus_bus es un registro del bus que ha pasado por la parada con ID_parada.
#La clave seria buscar por la ID_Parada y por el últimos timestamp de todas las lineas.
def getlast(table, n=1):
    q = "SELECT * FROM " + table + " ORDER BY ts DESC LIMIT " + str(n) + ";"
    cur = globals.mysql.connection.cursor()
    cur.execute(q)
    result = cur.fetchall()
    globals.mysql.connection.commit()
    return result

#INSEREIX A LA TAULA ESPECIFICADA ELS VALORS ESPECIFICATS (values HA DE SER UN VECTOR AMB ELS VALORS EN ORDRE)
def insert(table, values):
    q = "INSERT INTO " + table + " VALUES("
    for i in range(len(values)-1):
        q = q + str(values[i]) + ','
    q = q + str(values[len(values)-1]) + ');'
    cur = globals.mysql.connection.cursor()
    cur.execute(q)
    result = cur.fetchall()
    cur.close()
    globals.mysql.connection.commit()
    return result

# LA IDEA ÉS FER UN THREAD PER A CADA "SENSOR VIRTUAL". COMPORTAMENT DE CADA TIPUS DE SENSOR DEFINIT A classes.py
def initsensors():
    #hacer array de buses bus[i], recorrer un array de lineas de bus ('L69', 'L70'...) Runearlos TODOS de una.
    #El 0 representa el id_bus. Tiene que ser valor único.

    bus = autobus_bus(30, 0, 'L69')
    t = Thread(target=bus.run)
    t.start()

    # soilmoisture(N, id_sensor, latitud, longitud)
    sensor_humitat = soilmoisture(100, 12, 46.52, 47.23)
    t1 = Thread(target=sensor_humitat.run)
    t1.start()
    return 0


#DEVUELVE LAS PARADAS EN LAS QUE PARA UN BUS DE UNA DETERMINADA LÍNEA
def getparadas(linea):
    q = "SELECT parades FROM linies_info WHERE nom='" + linea + "';"
    cur = globals.mysql.connection.cursor()
    cur.execute(q)
    result = cur.fetchall()
    cur.close()
    globals.mysql.connection.commit()
    print(str(result).split("'")[1])
    res = str(result).split("'")[1]
    return res.split(',')
