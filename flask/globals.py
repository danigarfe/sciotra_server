from flask_mysqldb import MySQL
#UTILIZADO PARA COMPARTIR VARIABLES GLOBALES ENTRE ARCHIVOS 
def initializedb(app):
    global mysql 
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Sciotra1234'
    app.config['MYSQL_DB'] = 'bbdd'
    mysql = MySQL(app)