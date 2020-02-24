from app import app
from flask import Flask, Blueprint, make_response, jsonify, request, json

# from app import toollist
from pymongo import MongoClient

# include pprint for readabillity of the
from pprint import pprint

# Use dumps from bson.json_util:
from bson.json_util import dumps

# to delete tools by ObjectId
from bson.objectid import ObjectId


tools = Blueprint("tools", __name__)
# client = MongoClient(app.config["MONGO_URL"])
MONGO_DATABASE_URI = app.config["MONGO_DATABASE_URI"]
client = MongoClient(MONGO_DATABASE_URI, connect=False)

db = client.igo_tools


@tools.route("/getTools", methods=["GET", "POST"])
def get_tools():

    # gets sorted tools from MongoDB
    tools = dumps(db.tools.find().sort("name"))
    # print(tools)

    # returns the tools
    return make_response(tools, 200)


@tools.route("/addTool", methods=["POST"])
def add_tool():

    # gets the data from the front end
    new_tool = request.json
    # print(new_tool)

    # adds new tool as a new toolsDB collection
    tools = db.tools.insert(new_tool)

    # gets updated list of tools
    current_tools = dumps(tools)

    # returns the tools
    return make_response(current_tools, 200)


@tools.route("/deleteTool", methods=["POST"])
def delete_tool():

    # gets the tool for which the delete button was clicked
    # pprint(request.json)
    old_tool = request.json

    # gets the id of the tool
    id = old_tool.get("id", None)
    # print(id)

    # deletes that collection from the db
    updated_tools = db.tools.delete_one({"_id": ObjectId(id)})

    # gets updated list of tools
    current_tools = dumps(db.updated_tools.find())

    # returns the tools
    return make_response(current_tools, 200)


@tools.route("/editTool", methods=["POST"])
def edit_tool():

    # gets the tool for which the edit button was clicked
    edit_tool = request.json

    # gets the id of the tool
    id = edit_tool.get("_id", None)
    oid = id["$oid"]
    # print(oid)

    # remove id to make mongo happy
    edit_tool.pop("_id")

    # edits that collection from toolsDB by its id
    updated_tools = db.tools.update_one(
        {"_id": ObjectId(oid)}, {"$set": edit_tool})

    # gets updated list of tools
    current_tools = dumps(db.tools.find())

    # return the toollist
    return make_response(current_tools, 200)
