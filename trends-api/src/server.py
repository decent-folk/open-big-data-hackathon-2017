from flask import Flask
from flask import request
from flask import abort
from flask import make_response

import json

import pytrends
from pytrends.request import TrendReq

import pandas

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

    pytrends = TrendReq(
        "hackathonspb@gmail.com",
        "qwertyqwerty",
        hl='en-US',
        tz=360,
        custom_useragent=None
    )

    pytrends.build_payload(
        [skill],
        cat=0,
        timeframe='today 5-y',
        geo='',
        gprop=''
    )

    interest_over_time_df = pytrends.interest_over_time()

    resp = make_response(interest_over_time_df.to_json(
        path_or_buf=None,
        orient=None,
        date_format='epoch',
        double_precision=10,
        force_ascii=True,
        date_unit='ms',
        default_handler=None,
        lines=False)
    )

    resp.headers['Access-Control-Allow-Origin'] = "*"

    return resp
