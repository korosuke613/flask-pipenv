from flask import Flask, render_template
from flask_restful import Api
from apis import hello_world, todo, version, timecapsule_api

app = Flask(__name__)
api = Api(app)
api_url = '/api'
timecapsule_url = api_url + '/timecapsule'
api.add_resource(hello_world.HelloWorld, '/hello')
api.add_resource(todo.TodoSimple, '/todos/<string:todo_id>')
api.add_resource(todo.TodoList, '/todos')
api.add_resource(version.Version, '/version')
api.add_resource(timecapsule_api.TimeCapsuleUserApi, timecapsule_url + '/user')
api.add_resource(timecapsule_api.TimeCapsuleUserEventApi, timecapsule_url + '/event/<string:user_id>')
api.add_resource(timecapsule_api.TimeCapsuleUserDetailApi, timecapsule_url + '/user/<string:user_id>')
api.add_resource(timecapsule_api.TimeCapsuleEventApi, timecapsule_url + '/event')


@app.route('/')
def index():
    return render_template('sample_api_load.html')


@app.route('/registration')
def registration():
    return render_template('HtmlPage01.html')


@app.route('/reservation')
def reservation():
    return render_template('HtmlPage02.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
