from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import users_model

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/api/v1')
user = users_model.UserModels()


@user_blueprint.route('/signup', methods=['POST'])
def singup():
    """ endpoint for signing up user """

    data = request.get_json()
    if not data:
        return(jsonify({"message": "Data set cannot be empty"}), 404)
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    account_type = data.get('account_type')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    res = jsonify(user.signup_user(first_name, last_name,
                                   account_type, username, email, password))
    res.status_code = 201
    return res


@user_blueprint.route('/signin', methods=['POST'])
def signin():
    """ endpoint for signing in user """

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    res = jsonify(user.singin_user(username, password))
    res.status_code = 200
    return res
