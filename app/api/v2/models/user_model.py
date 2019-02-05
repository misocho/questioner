from datetime import datetime
from app.api.v2.utils.validations import Validations
from app.database.db_con import QuestionerDB

validate = Validations()


class Users:
    """ Contains methods for user models """

    def signup(self, firstname, lastname, othername, email, phoneNumber, username, password , isAdmin=False):
        """ creates user signup model """


        query = """ INSERT INTO users (firstname, lastname, othername, email, phoneNumber,
                username, password, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING firstname, lastname, othername, email, phoneNumber,
                username, isAdmin"""

        data = (firstname, lastname, othername, email, phoneNumber,
                username, password, isAdmin)

        return QuestionerDB.save(query, data)

    def signin(self, userdata, username):
        """ creates user signin model """

        query = " SELECT {} FROM users WHERE username = '{}' ".format(
            userdata, username)
        return QuestionerDB.fetch_one(query)

    @classmethod
    def check_isAdmin(cls, username):
        """ checks if user is an admin """

        query = "SELECT isAdmin FROM users WHERE username = '{}'".format(
            username)

        return QuestionerDB.fetch_one(query)
