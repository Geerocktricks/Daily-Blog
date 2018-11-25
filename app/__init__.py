from flask import Flask , flash , redirect, url_for , session ,logging
from flask_bootstrap import Bootstrap
from .data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

# Initializ ing application
app = Flask(__name__)

Articles = Articles ()

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views