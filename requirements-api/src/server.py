from flask import Flask
from flask import request
from flask import abort
from flask import make_response

import json

from main import HeadHunterSiteParser
from main import distance

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    return "Bad request :("

@app.errorhandler(404)
def bad_request(error):
    return "Not found :("

@app.route("/getRequirements")
def get_requirements():
    name = request.args.get('name').encode('utf-8')
    if (name is None):
        abort(400)

    parser = HeadHunterSiteParser()
    requirenments = parser.get_all_requirenments({"text":name, "search_field":"name"})

    resp = make_response(json.dumps({"name":name,"requirements":requirenments}))
    resp.headers['Access-Control-Allow-Origin'] = "*"

    return resp

@app.route("/getDistance")
def get_distance():
    word1 = request.args.get('a').encode('utf-8')
    word2 = request.args.get('b').encode('utf-8')

    resp = make_response(str(distance(a, b)))
    resp.headers['Access-Control-Allow-Origin'] = "*"

    return resp
