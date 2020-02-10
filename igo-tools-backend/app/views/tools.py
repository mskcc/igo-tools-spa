from flask import Flask, Blueprint, make_response, jsonify, request, json
# from app import toollist
from pymongo import MongoClient
# include pprint for readabillity of the
from pprint import pprint
# Use dumps from bson.json_util:
from bson.json_util import dumps


tools = Blueprint("tools", __name__)
client = MongoClient("mongodb://bItAndAL:stONTICe@localhost:27017/toolsDB")
# MONGO_DATABASE_URI = app.config["MONGO_DATABASE_URI"]
# client = MongoClient(MONGO_DATABASE_URI)

db = client.toolsDB


@tools.route("/getTools", methods=["GET", "POST"])
def get_tools():

    # get tools from MongoDB
    tools = dumps(db.tools.find())
    # pprint(tools)
    return make_response(tools, 200)


@tools.route("/addTool", methods=["POST"])
def add_tool():

    # get the data from the front end
    new_tool = request.json
    print(new_tool)

    # add new tool as a new toolsDB collection
    tools = db.tools.insert(new_tool)

    # get updated list of tools
    current_tools = dumps(tools)

    # return the toollist
    return make_response(current_tools, 200)


@tools.route("/deleteTool", methods=["POST"])
def delete_tool():

    # get the tool for which the delete button is being clicked
    # pprint(request.json)
    old_tool_name = request.json
    text = old_tool_name.get("name", None)
    print(text)

    # delete that collection from toolsDB
    tools = db.tools.delete_one({"name": text})
    # tools = db.tools.remove({"name": "text"})

    # get updated list of tools
    current_tools = dumps(db.tools.find())

    # return the toollist
    return make_response(current_tools, 200)
