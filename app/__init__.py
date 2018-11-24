from flask import Flask
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views