from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import users_model
from ....validators import validator


user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/api/v1/auth')
user = users_model.UserModels()
user_validation = validator.BaseValidations()


@user_blueprint.route('/signup', methods=['POST'])
def singup():
    """ endpoint for signing up user """

    try:
        data = request.get_json() if request.is_json else None
    except Exception:
        return jsonify({"message": "data not in json"}), 400

    if not data:
        return(jsonify({"message": "Data set cannot be empty"}), 400)

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    isAdmin = data.get('isAdmin')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    

    res = user.signup_user(first_name, last_name, username,  email, password, isAdmin)
    
    return res


@user_blueprint.route('/signin', methods=['POST'])
def signin():
    """ endpoint for signing in user """

    try:
        data = request.get_json() if request.is_json else None
    except Exception:
        return jsonify({"message": "data not in json"}), 400

    if data:
        username = data.get('username')
        password = data.get('password')

    

    else:
       return jsonify({"message" : "Data set cannot be empty"}), 400
    res = user.singin_user(username, password)
    return res
