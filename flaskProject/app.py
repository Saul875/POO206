
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb


app= Flask(__name__)

app.config['MYSQL_Host']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="root"
app.config['MYSQL_DB']="dbflask"
#app.config['MYSQL_POR']="<puerto en el que se encuentra>"    (solo en caso de haber cambiado el puerto)

mysql= MySQL(app)
#Ruta para revisar conexión a MYSQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify ({'status':'ok','message':'Concetado con exito'}),200
    except Exception as e:
        return jsonify ({'status':'ok','message': str(e)}),500 


#Ruta simple
@app.route('/')
def home():
    return 'hola mundo FLASK'

#Ruta con parámetros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return '<h1><marquee>Un saludo a ' + nombre + '</marquee></h1>'

#Ruta try catch
@app.errorhandler(404)
def pagNoE(e):
    return 'La princesa está en otro castillo', 404

#ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def doubleroute():
    return 'Soy el mismo recurso del servidor'

#ruta POST
@app.route('/formulario', methods=['POST'])
def formulario():
    return 'Soy un formulario'

if __name__ == '__main__':
    app.run(port=3000,debug=True) 
    
    