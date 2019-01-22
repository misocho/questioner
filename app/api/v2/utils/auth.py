import jwt
from functools import wraps
from datetime import datetime
from flask import request
from app.api.v2.models.user_model import Users


class Auth:
    """ Class for authenticating users """

    def generate_token(self, username, isAdmin):
        """ Method for generating token """

        session = datetime.now() + datetime.timedelta(minutes=30)
        token_details = {
            'username': username,
            'isAdmin': isAdmin,
            'session': session
        }

        token = jtw.encode(token_details, algorith='HS256')

        return token
