from flask import Flask
from flask_mysqldb import MySQL
from functions import *
app = Flask(__name__)
'''
PER EXECUTAR, A LA CARPETA /flask FEM:
pip install flask
pip install flask_mysqldb
flask run

EXEMPLE D'ÚS MYSQL:
cur = mysql.connection.cursor()
cur.execute("INSERT INTO MyUsers(firstName, lastName)........")
mysql.connection.commit()
'''

#MYSQL DATABASE CONFIGURATION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sciotra1234'
app.config['MYSQL_DB'] = 'bbdd'
mysql = MySQL(app)

#INICIA EL SENSORS
initsensors(mysql)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/last')
def last():
    taula = request.args.taula
    result = getlast(taula, mysql)
    return result

@app.route('/put')
def put():
    insert('autobus_bus', [0,1,3,"'L40'",'NULL'], mysql)
    return 'OK'


