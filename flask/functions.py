from classes import *

#OBTÉ LA DARRERA ENTRADA DE LA BASE DE DADES DE LA TAULA ESPECIFICADA
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
    bus = autobus_bus(30, 0, 'L69')
    t = Thread( target=bus.run )
    t.start()
    return 0
