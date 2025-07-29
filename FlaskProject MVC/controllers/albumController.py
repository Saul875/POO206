from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.albumModel import *

albumsBP = Blueprint('albums', __name__, url_prefix='/')


# Ruta de inicio (consultar todos)
@albumsBP.route('/')
def home():
    try:
        consultaTodo = getAll()
        return render_template('formulario.html', errores={}, albums=consultaTodo)
    except Exception as e:
        print(f'Error al consultar todo {e}')
        flash('Error al cargar los álbumes')
        return render_template('formulario.html', errores={}, albums=[])


# Ruta para guardar álbumes
@albumsBP.route('/guardarAlbum', methods=['POST'])
def guardar():
    errores = {}
    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()

    if not Vtitulo:
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
    if not Vartista:
        errores['txtArtista'] = 'Artista obligatorio'
    if not Vanio:
        errores['txtAnio'] = 'Año obligatorio'
    elif not Vanio.isdigit() or int(Vanio) < 1800 or int(Vanio) > 2100:
        errores['txtAnio'] = 'Ingresa un año válido'

    if errores:
        return render_template('formulario.html', errores=errores, albums=getAll())

    try:
        InsertAlbum(Vtitulo, Vartista, Vanio)
        flash('Álbum guardado correctamente')
        return redirect(url_for('albums.home'))
    except Exception as e:
        flash(f'Error al guardar: {str(e)}')
        return redirect(url_for('albums.home'))


# Ruta para ver detalle
@albumsBP.route('/detalle/<int:id>')
def detalle(id):
    try:
        consultaId = getById(id)
        if not consultaId:
            flash('Álbum no encontrado')
            return redirect(url_for('albums.home'))
        return render_template('consulta.html', album=consultaId)
    except Exception as e:
        import traceback
        traceback.print_exc()
        flash('Error al cargar el álbum')
        return render_template('formulario.html', errores={}, albums=getAll())


# Ruta para mostrar formulario de actualización
@albumsBP.route('/actualizarAlbum/<int:id>', methods=['GET'])
def mostrar_actualizar(id):
    try:
        consultaId = getById(id)
        if not consultaId:
            flash('Álbum no encontrado')
            return redirect(url_for('albums.home'))
        return render_template('formUpdate.html', album=consultaId)
    except Exception as e:
        flash('Error al cargar datos: ' + str(e))
        return redirect(url_for('albums.home'))


# Ruta para procesar actualización
@albumsBP.route('/actualizarAlbum/<int:id>', methods=['POST'])  # <-- minúscula corregida aquí
def actualizar(id):
    errores = {}

    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()

    if not Vtitulo:
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
    if not Vartista:
        errores['txtArtista'] = 'Artista obligatorio'
    if not Vanio:
        errores['txtAnio'] = 'Año obligatorio'
    elif not Vanio.isdigit() or int(Vanio) < 1800 or int(Vanio) > 2100:
        errores['txtAnio'] = 'Ingresa un año válido'

    if errores:
        return render_template('formUpdate.html', errores=errores, album=(id, Vtitulo, Vartista, Vanio))

    try:
        updateAlbum(id, Vtitulo, Vartista, Vanio)
        flash('Álbum actualizado correctamente')
        return redirect(url_for('albums.home'))
    except Exception as e:
        flash('Error al actualizar: ' + str(e))
        return redirect(url_for('albums.home'))


# Ruta para mostrar confirmación de eliminación
@albumsBP.route('/eliminar/<int:id>', methods=['GET'])
def mostrarEliminar(id):
    try:
        consultaId = getById(id)
        if not consultaId:
            flash('Álbum no encontrado')
            return redirect(url_for('albums.home'))
        return render_template('eliminar.html', album=consultaId)
    except Exception as e:
        flash('Algo falló: ' + str(e))
        return redirect(url_for('albums.home'))


# Ruta para confirmar y ejecutar eliminación (soft delete)
@albumsBP.route('/eliminar/<int:id>', methods=['POST'])
def confirmarEliminar(id):
    try:
        softDeleteAlbum(id)
        flash('Álbum eliminado correctamente')
    except Exception as e:
        flash('Error al eliminar: ' + str(e))
    return redirect(url_for('albums.home'))
