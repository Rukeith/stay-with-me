from flask import Blueprint
from flaskr.models.demo import queryData

api_blueprint = Blueprint('hello', __name__)


@api_blueprint.route('/hello', methods=['GET'])
def hello():
    queryData()
    return 'Hello, World!'