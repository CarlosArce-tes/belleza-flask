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

    return render_template('citas.html', nombre = nombre, apellido=apellido)