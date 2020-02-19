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
client = MongoClient(MONGO_DATABASE_URI)

db = client.toolsDB


@tools.route("/getTools", methods=["GET", "POST"])
def get_tools():

    # get tools from MongoDB
    tools = dumps(db.tools.find())
    # print(tools)
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
    pprint(request.json)
    old_tool = request.json
    # get the id of the tool
    id = old_tool.get("id", None)
    print(id)

    # delete that collection from toolsDB by its id
    updated_tools = db.tools.delete_one({"_id": ObjectId(id)})

    # get updated list of tools
    current_tools = dumps(db.updated_tools.find())

    # return the toollist
    return make_response(current_tools, 200)


@tools.route("/editTool", methods=["POST"])
def edit_tool():

    # get the tool for which the edit button is being clicked
    # print(request.data)
    print(request.json)
    edit_tool = request.json
    print(type(edit_tool))
    # get the id of the tool
    id = edit_tool.get("_id", None)
    oid = id["$oid"]
    print(oid)

    # name = edit_tool["name"]
    # link = edit_tool["link"]
    # description = edit_tool["description"]
    edit_tool.pop("_id")
    # pprint(json.dumps(edit_tool))

    # find the tool
    # old_tool = db.tools.find({"_id": ObjectId(id)})
    # pprint(old_tool)

    # edit that collection from toolsDB by its id
    # updated_tools = db.tools.replaceOne({"_id": ObjectId(id)}, edit_tool)
    updated_tools = db.tools.update_one(
        {"_id": ObjectId(oid)}, {"$set": edit_tool})

    current_tools = dumps(db.tools.find())
    # replace the values
    # updated_tool.name = old_tool.get("name", None)
    # updated_tool.link = old_tool.get("link", None)
    # updated_tool.description = old_tool.get("description", None)

    # get updated list of tools
    # current_tools = dumps(db.updated_tools.find())

    # return the toollist
    return make_response(current_tools, 200)


# @tools.route("/editTool", methods=["POST"])
# def edit_tool():

#     # get the tool for which edit button was clicked
#     # find the tool in the db
#     # display tool details in the create form
#     # update tools on submit
#     # return tools

#     # get updated list of tools
#     current_tools = dumps(db.tools.find())

#     # return the toollist
#     return make_response(current_tools, 200)
