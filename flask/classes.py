from threading import Thread
from time import sleep
from functions import *

#CADA TIPUS DE THREAD ÉS UNA CLASS
class autobus_bus:
    #N => MULTIPLICADOR DE TEMPS DEFINIT AL DOCUMENT DE CRITERIS DE SIMULACIÓ
    #id_bus => ID DEL SENSOR EN CONCRET
    #lin => LÍNEA D'AUTOBUS DEL SENSOR
    def __init__(self, N, id_bus, lin, parades):
        self.interval = (5/N) * 60 #interval d'execució en segons
        self.linia = lin
        self.id_bus=id_bus
        self.parades=parades
    #S'EXECUTA AL THREAD, BUCLE INFINIT AMB PARADES sleep() 
    def run(self):
        #PARADAS DEFINIDAS POR ORDEN DE APARICIÓN. (HACIA LA ROTONDA de Francesc Macià) DE LA PARADA 32 A LA 28, Y VUELTA DE LA (ROTONDA de Francesc Macià hacía ZONA UNIVERSITARÍA) PARADA 27 A LA 29.
        #Este número de paradas se refiere a las establecidas en Google Earth. No a la de los autobuses.
        #SIMULA UN BUS QUE VA DANDO VUELTAS CONSTANTEMENTE AL TRAMO DE DIAGONAL SELECCIONADO
        #parades = [32, 30, 2, 33, 5, 6, 7, 9, 13, 11, 15, 17, 18, 19, 21, 22, 26, 28, 27, 25, 24, 23, 20, 16, 14, 12, 10, 8, 4, 3, 1, 31, 29]
        count = 0
        #Aquí la clave sería ir guardando las llegadas de los buses a cada parada en especifico en la base de datos. Primero lo dejamos así y luego podemos subir el tiempo de simulación para no cargar tanto de datos la BBDD.
        while True:
            sleep(self.interval)
            print("HA LLEGADO EL BUS ID=" + str(self.id_bus) + " DE LA LÍNEA " + self.linia + " A LA PARADA " + str(self.parades[count%len(self.parades)]))
            count = count+1
            #Aquí hacer un insert de Autobus_bus.
            

