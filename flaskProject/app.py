
from flask import Flask, jsonify, render_template, request, flash, redirect,url_for
from flask_mysqldb import MySQL
import MySQLdb


app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="root"
app.config['MYSQL_DB']="DBFlask"
#app.config['MYSQL_POR']="<puerto en el que se encuentra>"    (solo en caso de haber cambiado el puerto)
app.config['SECRET_KEY']= 'HEILhitler'

mysql= MySQL(app)
#Ruta para revisar conexión a MYSQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify ({'status':'ok','message':'Concetado con exito'}),200
    except MySQLdb.MySQLError as e:
        return jsonify ({'status':'error','message': str(e)}),500 

#Ruta de inicio
@app.route('/')
def home():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM albumss WHERE state = 1')
        consultaTodo= cursor.fetchall()
        return render_template('formulario.html', errores={},albums=consultaTodo)

    except Exception as e:
        print(f'Error al consultar todo {e}')
        return render_template('formulario.html', errores ={},albums=[])

    finally:
        cursor.close()

#Ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta de guardarAlbum
@app.route('/guardarAlbum', methods=['POST'])
def guardar():
    #Obtener los datos a insertar
    Vtitulo= request.form.get('txtTitulo','').strip()
    Vartista= request.form.get('txtArtista','').strip()
    Vanio= request.form.get('txtAnio','').strip()

#Intentamos Ejecutar el instert
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('insert into albumss(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
        flash('Guardado en BD')
        return redirect(url_for('home'))
    
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo fallo: '+ str(e))

    finally:
        cursor.close()
        
    return render_template('formulario.html',errores={})

@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('SELECT * FROM albumss WHERE id = %s', (id,))

        consultaId= cursor.fetchone()
        return render_template('consulta.html',albums=consultaId)
    
    except Exception as e:
        print('Error al consultar por id: '+ e)
        return redirect(url_for('home'))

    finally:
        cursor.close()
        
@app.route('/actualizarAlbum/<int:id>', methods=['GET'])
def mostrar_actualizar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM albumss WHERE id=%s', (id,))
        album = cursor.fetchone()
        return render_template('formUpdate.html', album=album)
    except Exception as e:
        flash('Error al cargar datos: ' + str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()
        
@app.route('/actualizarAlbum/<int:id>', methods=['POST'])
def actualizar(id):
    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()

    if not Vtitulo or not Vartista or not Vanio:
        flash('Todos los campos son obligatorios')
        return redirect(url_for('mostrar_actualizar', id=id))

    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE albumss SET titulo=%s, artista=%s, anio=%s WHERE id=%s', (Vtitulo, Vartista, Vanio, id))
        mysql.connection.commit()
        flash('Álbum actualizado correctamente')
        return redirect(url_for('home'))
    except Exception as e:
        mysql.connection.rollback()
        flash('Error al actualizar: ' + str(e))
        return redirect(url_for('mostrar_actualizar', id=id))
    finally:
        cursor.close()

@app.route('/eliminar/<int:id>', methods = ['GET'])
def mostrarEliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM albumss WHERE id=%s', (id,))
        album = cursor.fetchone()
        if not album:
            flash('Álbum no encontrado')
            return redirect(url_for('home'))
        return render_template('eliminar.html', album=album) 
    except Exception as e:
        flash('Algo falló: ' + str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()

@app.route('/eliminar/<int:id>', methods = ['POST'])
def confirmarEliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE albumss SET state = 0 WHERE id=%s', (id,))
        mysql.connection.commit()
        flash('Álbum eliminado en BD')
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo falló: ' + str(e))
    finally:
        cursor.close()
    return redirect(url_for('home'))

# #Ruta con parámetros
# @app.route('/saludo/<nombre>')
# def saludar(nombre):
#     return '<h1><marquee>Un saludo a ' + nombre + '</marquee></h1>'

#Ruta try catch
@app.errorhandler(404)
def pagNoE(e):
    return 'La princesa está en otro castillo', 404

if __name__ == '__main__':
    app.run(port=3000,debug=True) 