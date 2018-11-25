from flask import Flask
from flask_bootstrap import Bootstrap
from .data import Articles

# Initializing application
app = Flask(__name__)

Articles = Articles ()

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views