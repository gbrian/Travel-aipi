# https://spapas.github.io/2014/06/30/rest-flask-mongodb-heroku/
import os
from flask import Flask
from flask.ext import restful
from flask import make_response
import json

app = Flask(__name__)

def output_json(obj, code, headers=None):
    resp = make_response(json.dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import flask_rest_service.resources