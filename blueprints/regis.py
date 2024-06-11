from flask import Blueprint, render_template, request, redirect, session, url_for, flash, make_response
import mysql.connector
from config.config import MYSQL_CONFIG


regis = Blueprint('regis', __name__)


@regis.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        executor = conn.cursor()
        executor.execute('select * from usuarios where usuario = %s and password = %s', (usuario, password))
        datosUser = executor.fetchone()
        if datosUser:
            
            session['nombres'] = datosUser[1]
            session['apellidos'] = datosUser[2]
            session['telefono'] = datosUser[3]
            session['email'] = datosUser[4]
            session['fecharegistro'] = datosUser[5]
            session['usuario'] = datosUser[6]
            session['password'] = datosUser[7]
            flash('¡Usuario registrado exitosamente!', 'success')
            return redirect(url_for('admin.panel'))
        else:
            error = 'Credenciales incorrectas o usuario no registrado'
            return render_template('login.html', error = error)
    return render_template('login.html')

@regis.route('logout')
def logout():
    session.clear()
    return redirect(url_for('index.inicio')) 
     

@regis.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        usuario = request.form['usuario']
        password = request.form['password']
        try:
            conn = mysql.connector.connect(**MYSQL_CONFIG)
            executor = conn.cursor()
            executor.execute('insert into usuarios (nombre, apellido, telefono, email, usuario, password)values (%s, %s, %s, %s, %s, %s)', (nombre, apellido, telefono, email, usuario, password))
            conn.commit()
            accedio = 'Registro exitoso'
            return render_template('registro.html', accedio=accedio)
        except Exception as e:
            error = 'Error al realizar el registro'
            return  render_template('registro.html', error=error)
         
    return render_template('registro.html')


'''
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    executor = conn.cursor()
    executor.execute('insert into usuarios (id, nombre, apellido, telefono, email, fecha_registro, usuario, password)values ()')
    
'''