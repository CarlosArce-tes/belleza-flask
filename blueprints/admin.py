'''
Blueprint de parte del usuario: Administrador
---------------------------------------------------------------------------------------------------------------------------------------------------------
Cada ruta representa los datos a los cuales el administrador es capaz de acceder

Panel de incio de las tareas que puede realizar usando un menu que redirecciona a las diferentes vistas creadas para este usuario
Vista de usuarios: El administrador puede agregar, eliminar, editar y ver los usuarios existentes en la plataforma
'''

from flask import Blueprint, render_template, session, redirect, url_for
admin = Blueprint('admin', __name__)
from config.config import MYSQL_CONFIG
import mysql.connector

@admin.route('/panel')
def panel():
    if 'user' and 'password' in session:
        nombre = session['nombres']
        apellido = session['apellidos']
        telefono = session['telefono']
        email = session['telefono']
        fecharegistro = session['fecharegistro']
        usuario = session['usuario']
        password = session['password']
    else:
        return redirect(url_for('index.inicio')), 
    return render_template('inicioadmin.html', usuario=usuario, nombre=nombre, apellido=apellido, telefono=telefono, email=email, fecharegistro=fecharegistro)

@admin.route('/usuarios')
def usuarios():
    if 'user' and 'password' in session:
        nombre = session['nombres']
        apellido = session['apellidos']
        telefono = session['telefono']
        email = session['telefono']
        fecharegistro = session['fecharegistro']
        usuario = session['usuario']
        password = session['password']

        conn = mysql.connector.connect(**MYSQL_CONFIG)
        executor = conn.cursor()
        executor.execute('select * from usuarios')
        users = executor.fetchall()
        #print(users)    //Impresion de usuairos para checar la conexion a la base de datos y ver que la peticion de datos sea exitosa, descomentar en caso de error de obtencion de usuarios, checar si la conexion es exitosa
    else: 
        
        return redirect(url_for('index.inicio'))

    return render_template('verusers.html', users=users, nombre=nombre, apellido=apellido, usuario=usuario)