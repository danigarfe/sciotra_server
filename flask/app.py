from flask import Flask, request, jsonify
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


#EJEMPLO PETICIÓN: GET /last?taula=autobus_bus&n=5 DEVUELVE LAS 5 ÚLTIMAS ENTRADAS DE autobus_bus (SEGÚN TIMESTAMP) EN JSON
@app.route('/last')
def last():
    taula = request.args.get("taula")
    if request.args.get("n") != "":
      n = request.args.get("n")
    result = getlast(taula, mysql, n)
    return jsonify(result)

@app.route('/put')
def put():
    insert('autobus_bus', [0,1,21,"'L40'",'NULL'], mysql)
    return 'OK'


