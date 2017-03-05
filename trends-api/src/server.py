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

@app.route("/getTrends")
def get_requirements():
    skill = request.args.get('skill')
    if (skill is None):
        abort(400)

    resp = make_response()
    resp.headers['Access-Control-Allow-Origin'] = "*"

    return resp
