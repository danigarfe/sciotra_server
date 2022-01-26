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
'''

#MYSQL DATABASE INIZIALIZATION
globals.initializedb(app)


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

#EJEMPLO PETICIÓN: GET /paradas?linea="N12" devuelve las paradas por las que pasa en JSON
@app.route('/paradas')
def paradas():
  result = getparadas(request.args.get("linea"))
  return jsonify(result)

#GET /init   inicia los threads de los sensores
@app.route('/init')
def init():
  initsensors(app)
  return "OK"

@app.route('/getCamera')
def getCamera():
  result = getlast("cameres")
  obj = {
    'ID' : result[0][1],
    'intensitat_transit' : result[0][2],
    'accident_flag' : result[0][3],
    'timestamp' : result[0][4]
  }
  return jsonify(obj)

@app.route('/getSoil')
def getSoil():
  results = getlastSoil()
  return jsonify(results)

@app.route('/getBike')
def getBike():
  results = getlastBike()
  return jsonify(results)

@app.route('/getBin')
def getBin():
  results = getlastBin()
  return jsonify(results)

@app.route('/getContaminacio')
def getContaminacio():
  results = getlastContaminacio()
  return jsonify(results)

@app.route('/getBus')
def getBus():
  results = getlastBus()
  return jsonify(results)