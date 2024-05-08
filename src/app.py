import sys
sys.path.append('../')
from flask import Flask, render_template
from config.config import MYSQL_CONFIG
from blueprints.index import index
from blueprints.regis import regis
from blueprints.admin import admin
import mysql.connector
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key='jsalkjdlksdhkhsadsdxczxc3156s4dasd46sad'
app.register_blueprint(index, url_prefix='/')
app.register_blueprint(regis, url_prefix='/regis')
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 