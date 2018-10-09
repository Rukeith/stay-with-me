from flask import Blueprint, render_template
from flaskr.models.demo import queryData

api_blueprint = Blueprint('hello', __name__, url_prefix='/hello')


@api_blueprint.route('/', methods=['GET'])
def hello():
    queryData()
    return 'Hello, World!'


@api_blueprint.route('/vv', methods=['GET'])
def vv():
    return render_template('index.html')