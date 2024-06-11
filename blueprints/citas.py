from flask import Flask, Blueprint, render_template, session
citas = Blueprint('citas', __name__)
from config.config import MYSQL_CONFIG
import mysql.connector

@citas.route('/vercitas')
def vercitas():
    if 'user' and 'password' in session:
        nombre = session['nombres']
        apellido = session['apellidos']
        telefono = session['telefono']
        email = session['telefono']
        fecharegistro = session['fecharegistro']
        usuario = session['usuario']
        password = session['password']
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        executor  = conn.cursor()
        executor.execute('select * from citas')
        datos_citas = executor.fetchall()
    return render_template('citas.html', nombre = nombre, apellido=apellido, datos_citas = datos_citas)