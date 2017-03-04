from flask import Flask
from flask import request
from flask import abort

import json

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    return "Bad request :("

@app.errorhandler(404)
def bad_request(error):
    return "Not found :("

@app.route("/getRequirements")
def get_requirements():
    name = request.args.get('name')
    if (name is None):
        abort(400)

    requirements = ["C++", "TDD"]
    json_data = json.dumps({"name":name,"requirements":requirements})

    return json_data
