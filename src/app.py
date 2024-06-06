#Importacion de librerias y direcciones

#Configuracion de carpetas para Distribuciones de Linux
import sys
sys.path.append('../')

#Configuracion de carpetas para Sistemas Operativos de Windows
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#Importacion de Flask y complementos
from flask import Flask, render_template

# Configuracion de MySQL
from config.config import MYSQL_CONFIG

# Importacion de Blueprints que estan el el directorio blueprins
from blueprints.index import index
from blueprints.regis import regis
from blueprints.admin import admin
from blueprints.citas import citas

# Importar conector de MySQL
import mysql.connector

# Creacion de app de Flask
app = Flask(__name__, template_folder='../templates', static_folder='../static')

#Clave secreta de seguridad (Pueden ser cualquier cadena de texto)
app.secret_key='jsalkjdlksdhkhsadsdxczxc3156s4dasd46sad'



# Registro en app cada uno de los blueprints
# Los Blueprints estan almacenados en la carpeta blueprints y se tienen que importar



'''
app.register_blueprint(nombre, url_prefix='como aparecera en la url')
'''
#Blueprint encargado de la pagina principal de la aplicacion
app.register_blueprint(index, url_prefix='/')
#Blueprint engargado de la autenticacion, login, registro y cierre de session de usuarios
app.register_blueprint(regis, url_prefix='/regis')
#Blueprint encargado de las tareas correspondientes o dirigen al perfil del administrador
app.register_blueprint(admin, url_prefix='/admin')

app.register_blueprint(citas, url_prefix='/citas')

# Inicializacion del servidor de Flask
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 