from flask import Blueprint, jsonify, make_response, request
from werkzeug.security import generate_password_hash

from ..models.user_model import Users

auth = Blueprint('auth', __name__, url_prefix='/api/v2/auth')

user = Users()


auth.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()

    except:
        return jsonify({
            "status" : 400,
            "message" : "Invalid input"
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

    res = user.signup(firstname, lastname, othername, email, phoneNumber, username, password, isAdmin)
    
    return jsonify(res, {
        "status" : 201,
        "message" : "registration was successful"
    }) , 201
