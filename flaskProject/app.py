
from flask import Flask

app= Flask(__name__)

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