from flask import Flask
from flask import request
from flask import abort
from flask import make_response

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

    resp = make_response(json.dumps({"name":name,"requirements":requirements}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
