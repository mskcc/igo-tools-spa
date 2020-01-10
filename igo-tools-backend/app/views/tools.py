from flask import Flask, Blueprint, make_response, jsonify
from app import toollist

tools = Blueprint("tools", __name__)


@tools.route("/getTools")
def get_tools():
    return make_response(jsonify(toollist.tools), 200)
