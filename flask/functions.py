from classes import *

def getlast(table, mysql):
    q = "SELECT * FROM " + table + " ORDER BY id DESC LIMIT 1;"
    cur = mysql.connection.cursor()
    cur.execute(q)
    result = cur.fetchall()
    mysql.connection.commit()
    return result

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

def initsensors(mysql):
    bus = autobus_bus(30, 0, 'L69')
    t = Thread( target=bus.run )
    t.start()
    return 0
