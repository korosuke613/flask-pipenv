from flask import request
from flask_restful import Resource
from apis import timecapsule_db

# call like
"""
curl http://127.0.0.1:5000/todos/todo1 -d "data=Remember the milk" -X PUT
curl http://127.0.0.1:5000/todo1
curl http://127.0.0.1:5000/todos/todo2 -d "data=Change my brakepads" -X PUT
curl http://127.0.0.1:5000/todo2
"""

todos = {}


class TimeCapsuleUserApi(Resource):
    def __init__(self):
        self.time_capsule = timecapsule_db.TimeCapsule()

    def get(self):
        print('aaa')
        pass

    def post(self):
        id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        mail_address = request.form['mail_address']
        password = request.form['password']
        self.time_capsule.add_user(id, name, address, mail_address, password)
        return {'message': 'OK'}, 200, {'Access-Control-Allow-Origin': '*'}


class TimeCapsuleUserEventApi(Resource):
    def __init__(self):
        self.time_capsule = timecapsule_db.TimeCapsule()

    def get(self, user_id):
        return self.time_capsule.get_user_event(user_id), 200, {'Access-Control-Allow-Origin': '*'}

class TimeCapsuleUserDetailApi(Resource):
    def __init__(self):
        self.time_capsule = timecapsule_db.TimeCapsule()

    def get(self, user_id):
        return self.time_capsule.get_user(user_id), 200,  {'Access-Control-Allow-Origin': '*'}

class TimeCapsuleEventApi(Resource):
    def __init__(self):
        self.time_capsule = timecapsule_db.TimeCapsule()

    def post(self):
        user_id = request.form['user_id']
        delivery_date = request.form['delivery_date']
        info = request.form['info']
        self.time_capsule.add_event(user_id, delivery_date, info)

        return {'message': 'OK'}, 200,  {'Access-Control-Allow-Origin': '*'}
