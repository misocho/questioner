from flask import Blueprint, jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash

from ..models.user_model import Users

auth = Blueprint('auth', __name__, url_prefix='/api/v2/auth')

user = Users()


@auth.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "message": "Data not in json"
        }), 400

    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othername = data.get('othername')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    username = data.get('username')
    isAdmin = data.get('isAdmin')
    password = data.get('password')

    password = generate_password_hash(password)

    res = user.signup(firstname, lastname, othername, email,
                      phoneNumber, username, password, isAdmin)
    return jsonify({
        "data": [res],
        "status": 201,
        "message": "registration was successful"
    }), 201


@auth.route('/signin', methods=['POST'])
def sigin():
    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "message": "Data not in json"
        })

    username = data.get('username')
    password = data.get('password')

    userdata = "id, firstname, lastname, username, password, email"

    data = user.signin(userdata, username)

    if data:
        check = check_password_hash(data['password'], password)
        if check:
            return jsonify({
                "status": 200,
                "message": "Successfully \
                signed is as {}".format(data['username'])
            }), 200

        else:

            return jsonify({
                "status": 401,
                "message": "Invalid password"
            }), 401

    else:
        return jsonify({
            "status": 404,
            "message": "User {} does not exist".format(username)
        }), 404
