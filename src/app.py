#Importacion de librerias y direcciones
import sys
sys.path.append('../')
from flask import Flask, render_template

# Configuracion de MySQL
from config.config import MYSQL_CONFIG

# Importacion de Blueprints que estan el el directorio blueprins
from blueprints.index import index
from blueprints.regis import regis
from blueprints.admin import admin

# Importar conector de MySQL
import mysql.connector

# Creacion de app de Flask
app = Flask(__name__, template_folder='../templates', static_folder='../static')

#Clave secreta de seguridad
app.secret_key='jsalkjdlksdhkhsadsdxczxc3156s4dasd46sad'

# Registro en app cada uno de los blueprints

'''
app.register_blueprint(nombre, url_prefix='como aparecera en la url')
'''
app.register_blueprint(index, url_prefix='/')
app.register_blueprint(regis, url_prefix='/regis')
app.register_blueprint(admin, url_prefix='/admin')

# Inicializacion del servidor de Flask
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 