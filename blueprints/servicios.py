from flask import Flask, render_template, redirect, Blueprint, session,jsonify, request, Response
import mysql.connector

servicios = Blueprint('servicios', __name__)
from config.config import MYSQL_CONFIG

@servicios.route('/verservicios')
def verservicios():
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
        executor.execute('select * from servicios')
        datos_servicios = executor.fetchall()
        return jsonify(datos_servicios)
    #return render_template('servicios.html', datos_servicios = datos_servicios)