from flask import Blueprint, render_template
import mysql.connector
from config.config import MYSQL_CONFIG
regis = Blueprint('regis', __name__)
@regis.route('/login')
def login():
    return render_template('login.html')
@regis.route('/registro')
def registro():
    return render_template('registro.html')