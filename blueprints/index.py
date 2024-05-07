from flask import Blueprint, render_template
import mysql.connector
from config.config import MYSQL_CONFIG
index = Blueprint('index', __name__)
@index.route('/')
def inicio():
    return render_template('index.html' )
