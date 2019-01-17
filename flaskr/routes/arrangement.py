from flask import request, Blueprint, render_template
from flaskr.models import User

api_blueprint = Blueprint('arrangement', __name__, url_prefix='/arrangement')


"""
@api {post} /arrangement Create a arrangement
@apiName SingUp
@apiGroup User

@apiParam {String} email Users email address
@apiParam {String} password Users password
"""
@api_blueprint.route('/arrangement', methods=['POST'])
def signup():
    content = request.json
    return 'Hello, World!'