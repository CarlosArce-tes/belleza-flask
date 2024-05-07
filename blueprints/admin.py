from flask import Blueprint, render_template, session
admin = Blueprint('admin', __name__)
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

    return render_template('inicioapp.html', usuario=usuario, nombre=nombre, apellido=apellido, telefono=telefono, email=email, fecharegistro=fecharegistro)