from flask import Blueprint, jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash

from ..models.user_model import Users
from app.api.v2.utils.auth import Auth
from app.api.v2.utils.validations import Validations

authenticate = Auth()
validate = Validations()

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

    required = ['firstname', 'lastname', 'othername', 'email',
                'phoneNumber', 'username', 'password']

###### checks if all required fields are provided #####
    for value in required:
        if not (data.get(value) and data.get(value).replace(' ', '')):
            return jsonify({
                "status": 400,
                "message": "Please provide {}".format(value)
            }), 400

    firstname = data.get('firstname').replace(' ', '')
    lastname = data.get('lastname').replace(' ', '')
    othername = data.get('othername').replace(' ', '')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    username = data.get('username').replace(' ', '')
    isAdmin = data.get('isAdmin')
    password = data.get('password')

    check_email = validate.check_exist('users', 'email', email)
    check_phonenumber = validate.check_exist(
        'users', 'phoneNumber', phoneNumber)
    check_username = validate.check_exist('users', 'username', username)
    # checks if username , phonemuber and password exists
    not_valid = (check_email or check_phonenumber or check_username)
    if not not_valid:
        password = generate_password_hash(password)

        res = user.signup(firstname, lastname, othername, email,
                          phoneNumber, username, password, isAdmin)

        # Generates token when user signs up
        token = authenticate.generate_token(username, isAdmin)

        return jsonify({
            "data": [{"token": token}, res],
            "status": 201,
            "message": "registration was successful"
        }), 201

    else:
        return not_valid


@auth.route('/signin', methods=['POST'])
def sigin():
    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "message": "Data not in json"
        })

    required = ['username', 'password']
    for value in required:
        if not (data.get(value) and data.get(value).replace(' ', '')):
            return jsonify({
                "status": 400,
                "message": "Please provide {}".format(value)
            }), 400

    username = data.get('username').replace(' ', '')
    password = data.get('password')

    userdata = "username, password"

    data = user.signin(userdata, username)

    if data:
        check = check_password_hash(data['password'], password)
        if check:
            isAdmin = user.check_isAdmin(username)
            token = authenticate.generate_token(username, isAdmin)
            return jsonify({
                "token": token,
                "status": 200,
                "message": "Successfully signed is as {}".format(data['username'])
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
