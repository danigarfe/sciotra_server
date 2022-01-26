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
    conn = globals.mysql.connection
    cur = conn.cursor()
    cur.execute(q)
    result = cur.fetchall()
    cur.close()
    globals.mysql.connection.commit()
    return result

# LA IDEA ÉS FER UN THREAD PER A CADA "SENSOR VIRTUAL". COMPORTAMENT DE CADA TIPUS DE SENSOR DEFINIT A classes.py
def initsensors(app):
    #hacer array de buses bus[i], recorrer un array de lineas de bus ('L69', 'L70'...) Runearlos TODOS de una.
    #El 0 representa el id_bus. Tiene que ser valor único.
    '''
    bus = autobus_bus(30, 'L69')
    t = Thread(target=bus.run)
    t.start()
    '''
    with app.app_context():
        #INICIO THREADS SENSORES DE HUMEDAD
        soilsensors = []
        for i in range(62): #62
            soilsensors.append(soilmoisture(i+1))
            Thread(target=soilsensors[i].run, kwargs={'app': app}).start()
        print("SENSORES DE HUMEDAD INICIADOS")
        # soilmoisture(N, id_sensor, latitud, longitud)

        bus1 = autobus_bus(1, "E30")
        bus2 = autobus_bus(2, "E79")
        bus3 = autobus_bus(3, "E97")
        bus4 = autobus_bus(4, "E98")
        bus5 = autobus_bus(5, "L51")
        bus6 = autobus_bus(6, "L57")
        bus7 = autobus_bus(7, "L61")
        bus8 = autobus_bus(8, "L63")
        bus9 = autobus_bus(9, "L68")
        bus10 = autobus_bus(10, "L97")
        Thread(target=bus1.run, kwargs={'app': app}).start()
        Thread(target=bus2.run, kwargs={'app': app}).start()
        Thread(target=bus3.run, kwargs={'app': app}).start()
        Thread(target=bus4.run, kwargs={'app': app}).start()
        Thread(target=bus5.run, kwargs={'app': app}).start()
        Thread(target=bus6.run, kwargs={'app': app}).start()
        Thread(target=bus7.run, kwargs={'app': app}).start()
        Thread(target=bus8.run, kwargs={'app': app}).start()
        Thread(target=bus9.run, kwargs={'app': app}).start()
        Thread(target=bus10.run, kwargs={'app': app}).start()
        print("BUSES INICIADOS")

        contamin1 = nodecontaminacio(1, "ruido")
        contamin2 = nodecontaminacio(2, "ruido")
        contamin3 = nodecontaminacio(3, "ruido")
        contamin4 = nodecontaminacio(4, "mix")
        contamin5 = nodecontaminacio(5, "ruido")
        contamin6 = nodecontaminacio(6, "ruido")
        contamin7 = nodecontaminacio(7, "ruido")
        contamin8 = nodecontaminacio(8, "ruido")
        contamin9 = nodecontaminacio(9, "ruido")
        contamin10 = nodecontaminacio(10, "ruido")
        contamin11 = nodecontaminacio(11, "ruido")
        contamin12 = nodecontaminacio(12, "mix")
        contamin13 = nodecontaminacio(13, "ruido")
        contamin14 = nodecontaminacio(14, "ruido")
        contamin15 = nodecontaminacio(15, "ruido")
        Thread(target=contamin1.run, kwargs={'app': app}).start()
        Thread(target=contamin2.run, kwargs={'app': app}).start()
        Thread(target=contamin3.run, kwargs={'app': app}).start()
        Thread(target=contamin4.run, kwargs={'app': app}).start()
        Thread(target=contamin5.run, kwargs={'app': app}).start()
        Thread(target=contamin6.run, kwargs={'app': app}).start()
        Thread(target=contamin7.run, kwargs={'app': app}).start()
        Thread(target=contamin8.run, kwargs={'app': app}).start()
        Thread(target=contamin9.run, kwargs={'app': app}).start()
        Thread(target=contamin10.run, kwargs={'app': app}).start()
        Thread(target=contamin11.run, kwargs={'app': app}).start()
        Thread(target=contamin12.run, kwargs={'app': app}).start()
        Thread(target=contamin13.run, kwargs={'app': app}).start()
        Thread(target=contamin14.run, kwargs={'app': app}).start()
        Thread(target=contamin15.run, kwargs={'app': app}).start()
        print("NODOS DE CONTAMINACIÓN INICIADOS")

        containerlist = []
        for i in range(33): 
            containerlist.append(containers(i+1))
            Thread(target=containerlist[i].run, kwargs={'app': app}).start()
        print("NODOS DE CONTENEDORES INICIADOS")
    
        bikestop1 = bike_stop(1)
        bikestop2 = bike_stop(2)
        bikestop3 = bike_stop(3)
        bikestop4 = bike_stop(4)
        bikestop5 = bike_stop(5)
        bikestop6 = bike_stop(6)
        bikestop7 = bike_stop(7)
        bikestop8 = bike_stop(8)
        bikestop9 = bike_stop(9)
        bikestop10 = bike_stop(10)
        bikestop11 = bike_stop(11)
        bikestop12 = bike_stop(12)
        bikestop13 = bike_stop(13)
        bikestop14 = bike_stop(14)
        bikestop15 = bike_stop(15)
        Thread(target=bikestop1.run, kwargs={'app': app}).start()
        Thread(target=bikestop2.run, kwargs={'app': app}).start()
        Thread(target=bikestop3.run, kwargs={'app': app}).start()
        Thread(target=bikestop4.run, kwargs={'app': app}).start()
        Thread(target=bikestop5.run, kwargs={'app': app}).start()
        Thread(target=bikestop6.run, kwargs={'app': app}).start()
        Thread(target=bikestop7.run, kwargs={'app': app}).start()
        Thread(target=bikestop8.run, kwargs={'app': app}).start()
        Thread(target=bikestop9.run, kwargs={'app': app}).start()
        Thread(target=bikestop10.run, kwargs={'app': app}).start()
        Thread(target=bikestop11.run, kwargs={'app': app}).start()
        Thread(target=bikestop12.run, kwargs={'app': app}).start()
        Thread(target=bikestop13.run, kwargs={'app': app}).start()
        Thread(target=bikestop14.run, kwargs={'app': app}).start()
        Thread(target=bikestop15.run, kwargs={'app': app}).start()
        print("NODOS DE PARADA BICICLETA INICIADOS")

        camera = camera(1)
        Thread(target=camera.run, kwargs={'app': app}).start()
        print("NODO DE CÁMARA INICIADO")

#DEVUELVE LAS PARADAS EN LAS QUE PARA UN BUS DE UNA DETERMINADA LÍNEA
def getparadas(linea):
    q = "SELECT parades FROM linies_info WHERE nom='" + linea + "';"
    cur = globals.mysql.connection.cursor()
    cur.execute(q)
    result = cur.fetchall()
    cur.close()
    globals.mysql.connection.commit()
    res = str(result).split("'")[1]
    return res.split(',')
