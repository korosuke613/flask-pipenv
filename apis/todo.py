from flask import request
from flask_restful import Resource

# call like
"""
curl http://127.0.0.1:5000/todos/todo1 -d "data=Remember the milk" -X PUT
curl http://127.0.0.1:5000/todo1
curl http://127.0.0.1:5000/todos/todo2 -d "data=Change my brakepads" -X PUT
curl http://127.0.0.1:5000/todo2
"""

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def post(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


class TodoList(Resource):
    def get(self):
        return todos
