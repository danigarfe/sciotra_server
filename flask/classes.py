from datetime import datetime
from threading import Thread
from flask_mysqldb import MySQL
from time import sleep
import globals
import functions
import random

#CADA TIPUS DE THREAD ÉS UNA CLASS
class autobus_bus:
    #N => MULTIPLICADOR DE TEMPS DEFINIT AL DOCUMENT DE CRITERIS DE SIMULACIÓ
    #id_bus => ID DEL SENSOR EN CONCRET
    #lin => LÍNEA D'AUTOBUS DEL SENSOR

    count_parada = 0
    timestamp = 0

    def __init__(self, id_bus, lin):
        self.interval = (5/globals.N) * 60 #interval d'execució en segons, tiempo entre parada y parada
        self.id_bus = id_bus
        self.linia = lin
        self.parades = functions.getparadas(self.linia)
        self.count_parada = round(random.uniform(0, len(self.parades)-1))
        
    #S'EXECUTA AL THREAD, BUCLE INFINIT AMB PARADES sleep() 
    def run(self, app):
        with app.app_context():
            while True:
                sleep(self.interval)
                now = datetime.now()
                self.timestamp = datetime.timestamp(now)
                functions.insert("autobus_bus", [0, self.id_bus,self.parades[self.count_parada], "'"+self.linia + "'", "NULL"])
                print("Bus " + self.linia + " llega a la parada " + self.parades[self.count_parada])
                self.count_parada = self.count_parada + 1
                if self.count_parada==len(self.parades):
                    self.count_parada=0
            
class soilmoisture:

    humitat = 0.0 # inicialització de la variable humitat com a float.
    is_pump = False  # Indiquem que la bomba d'aigua esta desactivada

    def __init__(self, id_sensor):
        self.interval_baixada = (25/globals.N) * 60  # interval d'execució en segons baixa la humitat
        self.interval_pujada = (5/globals.N) * 60 # interval d'execució en segons puja la humitat
        self.id_sensor = id_sensor # Identificador definit al Google Earth
        
    def run(self, app):
        with app.app_context():
            self.humitat = random.uniform(35, 55) #Aquí definim la humitat inicial del sensor
            #print("\n\nNivell d'humitat actual del sensor " + str(self.id_sensor) + ": " + str(self.humitat) + "\n\n")
            while True:
                sleep(self.interval_baixada)  # Dorm en aquest interval
                self.humitat = self.humitat - 1  # Baixa en 1% el nivell de la humitat del total (total:100%)
                functions.insert("soilmoisture", [0, self.id_sensor, self.humitat, 0, 'NULL'])
                #print("Han pasat " + str(int((self.interval_baixada*100)/60)) + " minuts. Nivell d'humitat actual: " + str(self.humitat) + "\n\n")
                if (self.humitat < 30):  # Si la humitat es menor al 30% s'activa la bomba d'aigua i es va incrementant l'humitat
                    is_pump = True
                    #print("\n\nS'ha activat la bomba d'aigua del sensor " + str(self.id_sensor) + "\n\n")
                    while is_pump: # Mentre la bomba d'agua sigui activa fes al següent...
                        # Mentre que l'humitat sigui menor al 60%, dorm l'interval_pujada i després augmenta l'humitat 15%.
                        if(self.humitat < 60):
                            sleep(self.interval_pujada)
                            self.humitat = self.humitat + 15
                            functions.insert("soilmoisture", [0, self.id_sensor, self.humitat, 1, 'NULL'])
                            #print("Han pasat " + str(int((self.interval_pujada*100)/60)) + " minuts. Nivell d'humitat actual: " + str(self.humitat) + "\n\n")
                        else:
                            is_pump = False # Apaguem la bomba d'aigua si l'humitat es major ó igual al 60%
                            #print("\n\nS'ha desactivat la bomba d'aigua.\n\n \ Nivell d'humitat estable\n\n")

'''
#CADA TIPUS DE THREAD ÉS UNA CLASS
class nodecontaminacio:

    def __init__(self, ID, tipo):
        self.ID = ID
        self.interval = (5/globals.N) * 60 #interval d'execució en segons, tiempo entre parada y parada
        self.tipo=tipo
        if tipo=="aire":
            self.valor = round(random.uniform(0, 150))
        else:
            self.valor = round(random.uniform(30, 100))
        
    #S'EXECUTA AL THREAD, BUCLE INFINIT AMB PARADES sleep() 
    def run(self, app):
        with app.app_context():
            if self.tipo==aire:
                while True:

            else:
                while True:

            while True:
                sleep(self.interval)
                now = datetime.now()
                self.timestamp = datetime.timestamp(now)
                functions.insert("autobus_bus", [0, self.id_bus,self.parades[self.count_parada], "'"+self.linia + "'", "NULL"])
                print("Bus " + self.linia + " llega a la parada " + self.parades[self.count_parada])
                self.count_parada = self.count_parada + 1
                if self.count_parada==len(self.parades):
                    self.count_parada=0

'''


