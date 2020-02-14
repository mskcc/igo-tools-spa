from flask import Flask

from flask_cors import CORS
# from pymongo import MongoClient

# from tools import tools

app = Flask(__name__)
app.config.from_pyfile("../secret_config.py")

# app.config.from_pyfile("../secret_config.py")
from .views.tools import tools
app.register_blueprint(tools)

CORS(app)

# base route to indicate system status
@app.route("/", methods=["GET"])
def index():
    return "IGO-Tools backend up and running."