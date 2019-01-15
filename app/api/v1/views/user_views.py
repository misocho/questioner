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
        return(jsonify({"message": "Data set cannot be empty"}), 404)

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    account_type = data.get('account_type')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not user_validation.input_provided(first_name):
        return jsonify({"message": "Please provide first_name"}), 400

    if not user_validation.input_provided(email):
        return jsonify({"message": "Please provide an email"}), 400

    if not user_validation.valid_email(email):
        return jsonify({"message": "Please provide a valid email address"}), 202
    
    if not user_validation.input_provided(last_name):
        return jsonify({"message" : "Please provide last_name"}) , 400

    if not user_validation.input_provided(password):
        return jsonify({"message" : "Please provide password"}) , 400


    if not user_validation.input_provided(username):
        return jsonify({"message" : "Please provide username"}) , 400
    if len(password) < 6:
        return jsonify({"message" : "Password should have a minimum of 6 characters"}) , 202
        
    if not user_validation.strong_pass(password):
        return jsonify({"message" : "Password should have atleast one uppercase, special character and digit"}) , 202

    

    res = user.signup_user(first_name, last_name,
                                   account_type, username, email, password)
    
    return res


@user_blueprint.route('/signin', methods=['POST'])
def signin():
    """ endpoint for signing in user """

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    response = user.singin_user(username, password)
    return response
