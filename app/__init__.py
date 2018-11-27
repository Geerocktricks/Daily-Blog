from flask import Flask , flash , redirect, url_for , request, session ,logging
from flask_bootstrap import Bootstrap
from .data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

# Initializ ing application
app = Flask(__name__)

# config MySQL
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = '1921'
app.config['MySQL_DB'] = 'DailyBlog'
app.config['MySQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

Articles = Articles ()

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
app.secret_key = '1921'