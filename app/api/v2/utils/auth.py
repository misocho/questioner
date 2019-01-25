import jwt
import os
from functools import wraps
from datetime import datetime, timedelta
from flask import request, jsonify
from app.api.v2.models.user_model import Users


class Auth:
    """ Class for authenticating users """

    def generate_token(self, username, isAdmin):
        """ Method for generating token """

        session = str(datetime.now() + timedelta(minutes=30))
        token_details = {
            'username': username,
            'isAdmin': isAdmin,
            'session': session
        }

        token = jwt.encode(token_details, os.getenv(
            "SECRET_KEY"), algorithm='HS256').decode('utf-8')

        return str(token)


def login_required(f):
    """ User authentication function """
    @wraps(f)
    def authenticate(*args, **kwargs):
        """ decorator for login authentication """
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            try:
                data = jwt.decode(
                    token, os.getenv("SECRET_KEY"),
                    algorithm='HS256'
                )
            except jwt.ExpiredSignatureError:
                return jsonify({
                    'status': 401,
                    'error': 'Your session has expired. Please login again'
                }), 401
            user = data['username']

            if user:
                return f(*args, **kwargs, current_user=user)
            return jsonify({
                "status": 404,
                "error": "User not found"
            }), 404

        else:
            return jsonify({
                "status": 401,
                "error": "You are not logged in. Please login"
            }), 401
    return authenticate


def admin_required(f):
    """ Admin authentication function """
    @wraps(f)
    def authent(*args, **kwargs):
        """ decorator for admin authentication """
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            try:
                data = jwt.decode(
                    token, os.getenv("SECRET_KEY"),
                    algorithm='HS256'
                )
            except jwt.ExpiredSignatureError:
                return jsonify({
                    'status': 401,
                    'error': 'Your session has expired. Please login again'
                }), 401
            isAdmin = data['isAdmin']
            user = data['username']
            if user:
                if isAdmin == True:  # checks if user is an admin
                    return f(*args, **kwargs, current_user=user)
                else:
                    return jsonify({
                        "status": 401,
                        "error": "You are not an admin user"
                    }), 401
            return jsonify({
                "status": 404,
                "error": "User not found"
            }), 404

        else:
            return jsonify({
                "status": 401,
                "error": "You are not logged in. Please login"
            }), 401
    return authent
