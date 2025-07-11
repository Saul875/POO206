from flask import Flask, jsonify, render_template, request, flash, redirect, url_for, session, send_file
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="root"
app.config['MYSQL_DB']="examenDos"
#app.config['MYSQL_POR']="<puerto en el que se encuentra>"    (solo en caso de haber cambiado el puerto)
app.config['SECRET_KEY']= 'HolaMundo'

mysqsl= MySQL(app)
 
@app.route('/DBCheck')
def DB_check():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')
        return jsonify({'status': 'ok', 'message': 'Conectado con éxito'}), 200
    except MySQLdb.MySQLError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.errorhandler(404)
def PagNoE(e):
    return 'CUIDADO: ERROR DE CAPA 8 ¡¡¡', 404

@app.route('/')
def home ():
    #Obtener los datos a insertar
    cursor = mysqsl.connection.cursor()
    if request.method == 'POST':
        restaurantes = request.form['restaurantes']
        tipo = request.form['tipo']
        comentario = request.form['comentario']
        calificacion = request.form['calificacion']

        # Validar que los datos no estén vacíos
        if not restaurantes or not tipo or not comentario or not calificacion:
            flash("Todos los campos son obligatorios.", 'error')
            return redirect('/')

       

    return render_template('formulario.html')

if __name__ == '__main__':
        app.run(port=3000,debug=True) 
