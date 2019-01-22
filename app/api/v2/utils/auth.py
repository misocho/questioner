import jwt
import os
from functools import wraps
from datetime import datetime, timedelta
from flask import request
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

        token = jwt.encode(token_details, os.getenv("SECRET_KEY"), algorithm='HS256')

        return str(token)
