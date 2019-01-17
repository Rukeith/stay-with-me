from flask import request, Blueprint, render_template
from flaskr.models import User

api_blueprint = Blueprint('user', __name__, url_prefix='/user')


"""
@api {post} /user/signup User Sign Up
@apiName SingUp
@apiGroup User

@apiParam {String} email Users email address
@apiParam {String} password Users password
"""
@api_blueprint.route('/signup', methods=['POST'])
def signup():
    content = request.json
    print(content['username'])
    return 'Hello, World!'


"""
@api {post} /user/login Request User Login
@apiName Login
@apiGroup User

@apiParam {String} email Users email address
@apiParam {String} password Users password
"""
@api_blueprint.route('/login', methods=['POST'])
def login():
    return 'User login'


"""
@api {get} /user/profile/:user_id Request User information
@apiName GetUser
@apiGroup User

@apiParam {String} user_id Users unique ID.
"""
@api_blueprint.route('/profile/<uuid:user_id>', methods=['GET'])
def get_profile(user_id):
    return render_template('index.html', name='profile')

"""
@api {put} /user/profile/:user_id Update User information
@apiName UpdateUser
@apiGroup User

@apiParam {String} user_id Users unique ID.
"""
@api_blueprint.route('/profile/<uuid:user_id>', methods=['PUT'])
def update_profile(user_id):
    return 'User update profile'