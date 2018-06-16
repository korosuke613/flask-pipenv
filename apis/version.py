from flask_restful import Resource

# call like
"""
curl -X GET "http://127.0.0.1:5000/hello"
curl -X POST "http://127.0.0.1:5000/hello"
curl -X put "http://127.0.0.1:5000/hello"
curl -X DELETE "http://127.0.0.1:5000/hello"
"""


# Hello World
class Version(Resource):
    def get(self):
        return {'version': 'v1'}
