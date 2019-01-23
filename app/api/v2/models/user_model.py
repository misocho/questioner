from datetime import datetime
import os
from psycopg2.extras import RealDictCursor

from ....database.db_con import connect, connect_test
from app.api.v2.utils.validations import Validations

validate = Validations()


class Users:
    """ Contains methods for user models """

    def signup(self, firstname, lastname, othername, email, phoneNumber, username, password, isAdmin=None):
        """ creates user signup model """

        if os.getenv('FLASK_ENV') == 'development':
            db = connect()
        else:
            db = connect_test()
        if isAdmin is None:
            isAdmin = False

        cursor = db.cursor(cursor_factory=RealDictCursor)
        query = """ INSERT INTO users (firstname, lastname, othername, email, phoneNumber,
                username, password, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING * """

        cursor.execute(query, (firstname, lastname, othername,
                               email, phoneNumber, username, password, isAdmin))
        user = cursor.fetchone()
        db.commit()
        cursor.close()

        return user

    def signin(self, userdata, username):
        """ creates user signin model """
        if os.getenv('FLASK_ENV') == 'development':
            db = connect()
        else:
            db = connect_test()
        cursor = db.cursor(cursor_factory=RealDictCursor)
        query = " SELECT {} FROM users WHERE username = '{}' ".format(
            userdata, username)
        cursor.execute(query)
        data = cursor.fetchone()
        return data

    @classmethod
    def check_isAdmin(cls, username):
        """ checks if user is an admin """
        db = connect()
        cursor = db.cursor(cursor_factory=RealDictCursor)
        query = "SELECT isAdmin FROM users WHERE username = '{}'".format(
            username)
        cursor.execute(query)
        isAdmin = cursor.fetchone()
        return isAdmin
