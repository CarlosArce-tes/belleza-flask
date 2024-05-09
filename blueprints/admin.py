from flask import Blueprint, render_template, session
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

    return render_template('inicioadmin.html', usuario=usuario, nombre=nombre, apellido=apellido, telefono=telefono, email=email, fecharegistro=fecharegistro)

@admin.route('/usuarios')
def usuarios():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    executor = conn.cursor()
    executor.execute('select * from usuarios')
    users = executor.fetchall()
    print(users)