from flask import Flask
from .views.tools import tools
from flask_cors import CORS
# from pymongo import MongoClient

# from tools import tools

app = Flask(__name__)

# app.config.from_pyfile("../secret_config.py")
app.register_blueprint(tools)

CORS(app)
