from extensions import mysql

def getAll():
    #Obtener todos los álbumes activos
    print("Ejecutando getAll()")  # <--- Añádelo temporalmente
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM albumss WHERE state = 1')
    result = cursor.fetchall()        
    cursor.close()
    return result

def getById(id):
    #"""Obtener un álbum por ID"""
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM albumss WHERE id = %s', (id,))
    result = cursor.fetchone()  
    cursor.close()
    return result

def InsertAlbum(Vtitulo, Vartista, Vanio):
    #"""Insertar un nuevo álbum"""
    cursor = mysql.connection.cursor()
    cursor.execute(
        'INSERT INTO albumss(titulo, artista, anio) VALUES(%s, %s, %s)',
        (Vtitulo, Vartista, Vanio)
    )
    mysql.connection.commit()
    cursor.close()

def updateAlbum(id, Vtitulo, Vartista, Vanio):
    #"""Actualizar un álbum existente"""
    cursor = mysql.connection.cursor()
    cursor.execute(
        'UPDATE albumss SET titulo=%s, artista=%s, anio=%s WHERE id=%s',
        (Vtitulo, Vartista, Vanio, id)
    )
    mysql.connection.commit()
    cursor.close()

def softDeleteAlbum(id):
    #"""Eliminación lógica de un álbum"""
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE albumss SET state = 0 WHERE id=%s', (id,))
    mysql.connection.commit()
    cursor.close()




# from app import mysql

# #metodo para obtener albums activos
# def getAll():

#     cursor= mysql.connection.cursor()
#     cursor.execute('SELECT * FROM albumss WHERE state = 1')
#     consultaTodo= cursor.fetchall()
#     cursor.close()
#     return consultaTodo

# #metodo para obtener album por ID
# def getById(id):
#     cursor= mysql.connection.cursor()
#     cursor.execute('SELECT * FROM albumss WHERE id = %s', (id,))
#     consultaId= cursor.fetchone()
#     cursor.close()
#     return consultaId

# #metodo para insertar un album
# def InsertAlbum(Vtitulo,Vartista,Vanio):
#     cursor= mysql.connection.cursor()
#     cursor.execute('insert into albumss(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
#     mysql.connection.commit()
#     cursor.close()

# #metodo para actualizar un album
# def updateAlbum(id,Vtitulo,Vartista,Vanio):
#     cursor = mysql.connection.cursor()
#     cursor.execute('UPDATE albumss SET titulo=%s, artista=%s, anio=%s WHERE id=%s', (Vtitulo, Vartista, Vanio, id))
#     mysql.connection.commit()
#     cursor.close()

# #metodo par eliminar un album
# def softDeleteAlbum(id):
#     cursor = mysql.connection.cursor()
#     cursor.execute('UPDATE albumss SET state = 0 WHERE id=%s', (id,))
#     mysql.connection.commit()
#     cursor.close()
