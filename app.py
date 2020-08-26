from flask import Flask
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)

DATA = {
    'places':
        ['rome',
         'london',
         'new york city',
         'los angeles',
         'brisbane',
         'new delhi',
         'beijing',
         'paris',
         'berlin',
         'barcelona']
}

class Places(Resource):
    def get(self):
        # return our data and 200 OK HTTP code
        return {'data': DATA}, 200

    def post(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True)
        args = parser.parse_args()

        # check if we already have the location in places list
        if args['location'] in DATA['places']:
            # if we do, return 401 bad request
            return {
                'message': f"'{args['location']}' already exists."
            }, 401
        else:
            # otherwise, add the new location to places
            DATA['places'].append(args['location'])
            return {'data': DATA}, 200

    def delete(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True)
        args = parser.parse_args()

        # check if we have given location in places list
        if args['location'] in DATA['places']:
            # if we do, remove and return data with 200 OK
            DATA['places'].remove(args['location'])
            return {'data': DATA}, 200
        else:
            # if location does not exist in places list return 404 not found
            return {
                'message': f"'{args['location']}' does not exist."
                }, 404


api.add_resource(Places, '/places')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))