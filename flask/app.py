from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from functions import *
from classes import *
import globals
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
globals.initializedb(app)

#print(getlast(table="autobus_bus"))


@app.route('/')
def index():
  return 'Server Works!'


#EJEMPLO PETICIÓN: GET /last?taula=autobus_bus&n=5 DEVUELVE LAS 5 ÚLTIMAS ENTRADAS DE autobus_bus (SEGÚN TIMESTAMP) EN JSON
@app.route('/last')
def last():
    if request.args.get("n") != None:
      n = request.args.get("n")
      result = getlast(request.args.get("taula"), n)
    else:
      result = getlast(request.args.get("taula"))
    return jsonify(result)

@app.route('/put')
def put():
    insert('autobus_bus', [0,1,21,"'L40'",'NULL'])
    return 'OK'


@app.route('/paradas')
def paradas():
  result = getparadas(request.args.get("linea"))
  return jsonify(result)

@app.route('/init')
def init():
  initsensors()
  return "OK"
