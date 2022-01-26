from datetime import datetime
from threading import Thread
from flask_mysqldb import MySQL
from time import sleep
import globals
import functions
import random
import json

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
                #print("Bus " + self.linia + " llega a la parada " + self.parades[self.count_parada])
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



class nodecontaminacio:
    #posibles tipos aire, ruido, mix
    def __init__(self, ID, tipo):
        self.ID = ID
        self.interval = (15/globals.N) * 60 #interval d'execució en segons, tiempo entre parada y parada
        if tipo=="aire":
            self.isICA = 1
            self.isNOISE = 0
            self.valorICA = round(random.uniform(0, 150))
            self.valorNOISE = 0
        
        if tipo=="ruido":
            self.isICA = 0
            self.isNOISE = 1
            self.valorICA = 0
            self.valorNOISE = round(random.uniform(30, 100))
        
        if tipo=="mix":
            self.isICA = 1
            self.isNOISE = 1
            self.valorICA = round(random.uniform(0, 150))
            self.valorNOISE = round(random.uniform(30, 100))

        
    #S'EXECUTA AL THREAD, BUCLE INFINIT AMB PARADES sleep() 
    def run(self, app):
        with app.app_context():
            while True:
                sleep(self.interval)
                if self.isICA==1:
                    r=random.uniform(0, 200)
                    if r<=self.valorICA:
                        A = -1
                    else:
                        A = 1
                    self.valorICA = self.valorICA+A*10
                if self.isNOISE==1:
                    r=random.uniform(0, 130)
                    if r<=self.valorNOISE:
                        B = -1
                    else:
                        B = 1
                    self.valorNOISE = self.valorNOISE+B*10
                functions.insert("contaminacio", [0, self.ID, self.isICA, self.isNOISE, self.valorICA, self.valorNOISE, 'NULL'])

class containers:
    #posibles tipos aire, ruido, mix
    def __init__(self, ID):
        self.ID = ID
        self.interval = (30/globals.N) * 60
        self.inorganic = round(random.uniform(0, 90))
        self.organic = round(random.uniform(0, 90))
        self.glass = round(random.uniform(0, 90))
        self.paper = round(random.uniform(0, 90))
        self.plastic = round(random.uniform(0, 90))
        

        
    #S'EXECUTA AL THREAD, BUCLE INFINIT AMB PARADES sleep() 
    def run(self, app):
        with app.app_context():
            while True:
                sleep(self.interval)
                r = random.uniform(0, 1)
                if r>0.5:
                    self.inorganic = self.inorganic+10
                r = random.uniform(0, 1)
                if r>0.5:
                    self.organic = self.organic+10
                r = random.uniform(0, 1)
                if r>0.5:
                    self.glass = self.glass+10
                r = random.uniform(0, 1)
                if r>0.5:
                    self.paper = self.paper+10
                r = random.uniform(0, 1)
                if r>0.5:
                    self.plastic = self.plastic+10
                if self.inorganic>=100:
                    self.inorganic=0
                if self.organic>=100:
                    self.organic=0
                if self.glass>=100:
                    self.glass=0
                if self.paper>=100:
                    self.paper=0
                if self.plastic>=100:
                    self.plastic=0
                listavalores = {'inorganic': self.inorganic,'organic': self.organic,'glass': self.glass,'paper': self.paper,'plastic': self.plastic}
                listastr = json.dumps(listavalores)
                functions.insert("contenidors", [0, self.ID, 5, "'" + listastr + "'", 'NULL'])

class bike_stop:
    
    def __init__(self, IDparada):
        self.interval = (10/globals.N) * 60
        self.IDparada = IDparada
        self.nombre_llocs = 20
        self.nombre_llocs_lliures = round(random.uniform(1, 19))
        self.nombre_llocs_ocupats = self.nombre_llocs - self.nombre_llocs_lliures
        
    #S'EXECUTA AL THREAD, BUCLE INFINIT AMB PARADES sleep() 
    def run(self, app):
        with app.app_context():
            while True:
                sleep(self.interval)
                r = random.uniform(0, 1)
                if self.nombre_llocs_ocupats == 20:
                    if r >= 0.2:
                        self.nombre_llocs_ocupats = self.nombre_llocs_ocupats - 1
                        self.nombre_llocs_lliures = self.nombre_llocs_lliures + 1
                elif self.nombre_llocs_lliures == 0:
                    if r >= 0.2:
                        self.nombre_llocs_lliures = self.nombre_llocs_lliures + 1
                        self.nombre_llocs_ocupats = self.nombre_llocs_ocupats - 1
                else:
                    if r>= 0.2 and r<= 0.6:
                        self.nombre_llocs_ocupats = self.nombre_llocs_ocupats + 1
                        self.nombre_llocs_lliures = self.nombre_llocs_lliures - 1
                    elif r>= 0.6 and r<= 1:
                        self.nombre_llocs_ocupats = self.nombre_llocs_ocupats - 1
                        self.nombre_llocs_lliures = self.nombre_llocs_lliures + 1

                functions.insert("bicicleta_stop", [0, self.IDparada, self.nombre_llocs, self.nombre_llocs_lliures, self.nombre_llocs_ocupats, "NULL"])

class camera:
    
    count_tointerval2 = 0

    def __init__(self, ID_camera):
        self.interval = (10/globals.N) * 60
        self.ID_camera = ID_camera
        self.intensitat_transit = round(random.uniform(0, 2))
        self.accident_flag = False
        
    #S'EXECUTA AL THREAD, BUCLE INFINIT AMB PARADES sleep() 
    def run(self, app):
        with app.app_context():
            count_tointerval2 = 1
            while True:
                sleep(self.interval)
                count_tointerval2 = count_tointerval2 + 1
                if count_tointerval2 < 50:
                    self.accident_flag = False
                    r = random.uniform(0, 1)
                    if r <= 0.3:
                        if self.intensitat_transit == 2:
                            new = 1
                        if self.intensitat_transit == 1:
                            new = random.choice([0,2]) 
                        if self.intensitat_transit == 0:
                            new = 1
                        self.intensitat_transit = new
                else: 
                    count_tointerval2 = 0
                    r = random.uniform(0, 1)
                    '''
                    ¿Cuándo quieres que vuelva el flag de accidente a False? En la próxima vuelta, o esperamos 2 vueltas de simulación de 10 min?
                    '''
                    if r >= 0.5:
                        self.accident_flag = True
                        self.intensitat_transit = 2
                functions.insert("cameres", [0, self.ID_camera, self.intensitat_transit, self.accident_flag, "NULL"])
