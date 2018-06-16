from flask import Flask
from flask_restful import Api
from apis import hello_world, todo, version

app = Flask(__name__)
api = Api(app)
api.add_resource(hello_world.HelloWorld, '/hello')
api.add_resource(todo.TodoSimple, '/todos/<string:todo_id>')
api.add_resource(todo.TodoList, '/todos')
api.add_resource(version.Version, '/version')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
