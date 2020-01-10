from flask import Flask
from .views.tools import tools
from flask_cors import CORS

# from tools import tools

app = Flask(__name__)
app.register_blueprint(tools)

CORS(app)
