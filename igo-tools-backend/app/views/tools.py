from flask import Flask, Blueprint, make_response, jsonify, request, json
from app import toollist
from pymongo import MongoClient
# include pprint for readabillity of the
from pprint import pprint
# Use dumps from bson.json_util:
from bson.json_util import dumps

tools = Blueprint("tools", __name__)
client = MongoClient("mongodb://bItAndAL:stONTICe@localhost:27017/toolsDB")

db = client.toolsDB


@tools.route("/getTools", methods=["GET", "POST"])
def get_tools():
    # read toollist
    # path = '/Users/patrunoa/workspace/igo-tools-spa/igo-tools-backend/app/toollist.py'
    # with open(path, 'r') as input:
    # tools = json.load(input)
    # return make_response(jsonify(tools), 200)

    tools = dumps(db.tools.find())
    # pprint(tools)
    return make_response(tools, 200)


@tools.route("/addTool", methods=["POST"])
def add_tool():

    # get the current tools
    path = '/Users/patrunoa/workspace/igo-tools-spa/igo-tools-backend/app/toollist.py'
    with open(path, 'r') as input:
        tools = json.load(input)
    # print(tools)

    # get the data from the front end
    data = request.json

    # append the data from the form to the current tools
    tools.append(data)
    print(tools)

    # write the tools to the file

    with open(path, 'w') as output:
        output.write(json.dumps(tools))
    # tools_file.close()

    # fo = open(path, 'r')
    # content = fo.readlines()
    # print(content)

    # with open(path, 'a') as output:
    #     output.write(json.dumps(data))
    # tools_file.close()

    # return the toollist
    return make_response(jsonify(tools), 200)
