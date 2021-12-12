from threading import Thread
from time import sleep
from functions import *
import random

#CADA TIPUS DE THREAD ÉS UNA CLASS
class autobus_bus:
    #N => MULTIPLICADOR DE TEMPS DEFINIT AL DOCUMENT DE CRITERIS DE SIMULACIÓ
    #id_bus => ID DEL SENSOR EN CONCRET
    #lin => LÍNEA D'AUTOBUS DEL SENSOR

    id_parada = ""

    def __init__(self, N, id_bus, lin, parades):
        self.interval = (5/N) * 60 #interval d'execució en segons
        self.id_bus = id_bus
        self.linia = lin
        self.parades = parades
        
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
            self.id_parada = self.parades[count % len(self.parades)]
            print("Aquí mostramos el ID de la parada actual: " + str(self.id_parada))
            count = count+1
            #Aquí hacer un insert de Autobus_bus.
            
class soilmoisture:

    humitat = 0.0 # inicialització de la variable humitat com a float.
    is_pump = False  # Indiquem que la bomba d'aigua esta desactivada

    def __init__(self, N, id_sensor, latitud, longitud):
        self.interval_baixada = (25/N) * 60  # interval d'execució en segons baixa la humitat
        self.interval_pujada = (5/N) * 60 # interval d'execució en segons puja la humitat
        self.id_sensor = id_sensor # Identificador definit al Google Earth
        self.latitud = latitud  # Posició del sensor
        self.longitud = longitud  # Posició del sensor
        
    def run(self):

        self.humitat = random.uniform(35, 55) #Aquí definim la humitat inicial del sensor
        print("\n\nNivell d'humitat actual del sensor " + str(self.id_sensor) + ": " + str(self.humitat) + "\n\n")
        while True:
            sleep(self.interval_baixada)  # Dorm en aquest interval
            self.humitat = self.humitat - 1  # Baixa en 1% el nivell de la humitat del total (total:100%)
            print("Han pasat " + str(self.interval_baixada*30) + " segons. Nivell d'humitat actual: " + str(self.humitat) + "\n\n")
            if (self.humitat < 30):  # Si la humitat es menor al 30% s'activa la bomba d'aigua i es va incrementant l'humitat
                is_pump = True
                print("\n\nS'ha activat la bomba d'aigua\n\n")
                while is_pump: # Mentre la bomba d'agua sigui activa fes al següent...
                    # Mentre que l'humitat sigui menor al 60%, dorm l'interval_pujada i després augmenta l'humitat 15%.
                    if(self.humitat < 60):
                        sleep(self.interval_pujada)
                        self.humitat = self.humitat + 15
                        print("Han pasat " + str(self.interval_pujada*30) + " segons. Nivell d'humitat actual: " + str(self.humitat) + "\n\n")
                    else:
                        is_pump = False # Apaguem la bomba d'aigua si l'humitat es major ó igual al 60%
                        print("\n\nS'ha desactivat la bomba d'aigua.\n\n \
                            Nivell d'humitat estable\n\n")
