# https://spapas.github.io/2014/06/30/rest-flask-mongodb-heroku/
import json
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from flask_rest_service import app, api
from src.models.accommodation.image.AccommodationImageService import AccommodationImageService 

class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK'
        }

class AccommodationImageServiceEndPoint(restful.Resource):
    def __init(self):
        self.service = AccommodationImageService()
    def get(self):      
        parser = reqparse.RequestParser()
        parser.add_argument('img')
        args = parser.parse_args()
        prediction = self.service.predict(args['img'])  
        return {
            'status': 'OK',
            'args': args,
            'prediction': prediction
        }


api.add_resource(Root, '/')
api.add_resource(AccommodationImageServiceEndPoint, '/accommodation/image/classify/')
#api.add_resource(Reading, '/readings/<ObjectId:reading_id>')