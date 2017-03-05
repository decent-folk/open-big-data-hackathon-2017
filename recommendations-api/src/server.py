from flask import Flask
from flask import request
from flask import abort
from flask import make_response

import json

from recommendations import UdacitySiteParser

usp = UdacitySiteParser() #Cache
usp.get_courses()

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    return "Bad request :("

@app.errorhandler(404)
def bad_request(error):
    return "Not found :("

@app.route("/getCourses")
def get_courses():
    skill = request.args.get('skill')
    if (skill is None):
        abort(400)

    data = usp.find_courses(skill)

    resp = make_response(json.dumps({"skill":skill,"recommendations":data}))
    resp.headers['Access-Control-Allow-Origin'] = "*"

    return resp

@app.route("/getBooks")
def get_books():
    title = request.args.get('title')
    if (title is None):
        abort(400)

    k = KnigafundSiteParser()
    data = k.get_all_books('q':title, 'key':'AIzaSyCGUpmY-WKdrFiY_TJwt9gHZq9-6WoOwPM')

    resp = make_response(json.dumps({"title":title,"recommendations":data}))
    resp.headers['Access-Control-Allow-Origin'] = "*"

    return resp
