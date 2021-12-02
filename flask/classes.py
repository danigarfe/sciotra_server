from threading import Thread
from time import sleep
from functions import *

#CADA TIPUS DE THREAD ÉS UNA CLASS
class autobus_bus:
    #N => MULTIPLICADOR DE TEMPS DEFINIT AL DOCUMENT DE CRITERIS DE SIMULACIÓ
    #id => ID DEL SENSOR EN CONCRET
    #lin => LÍNEA D'AUTOBUS DEL SENSOR
    def __init__(self, N, id, lin):
        self.interval = (5/N) * 60 #interval d'execució en segons
        self.linia = lin
        self.id=id
    #S'EXECUTA AL THREAD, BUCLE INFINIT AMB PARADES sleep() 
    def run(self):
        #PARADAS DEFINIDAS POR ORDEN DE APARICIÓN. HACIA LA ROTONDA DE LA PARADA 32 A LA 28, Y VUELTA DE LA PARADA 27 A LA 29.
        #SIMULA UN BUS QUE VA DANDO VUELTAS CONSTANTEMENTE AL TRAMO DE DIAGONAL SELECCIONADO
        parades = [32, 30, 2, 33, 5, 6, 7, 9, 13, 11, 15, 17, 18, 19, 21, 22, 26, 28, 27, 25, 24, 23, 20, 16, 14, 12, 10, 8, 4, 3, 1, 31, 29]
        count = 0
        while True:
            sleep(self.interval)
            print("HA LLEGADO EL BUS ID=" + str(self.id) + " DE LA LÍNEA " + self.linia + " A LA PARADA " + str(parades[count%len(parades)]))
            count = count+1
            

