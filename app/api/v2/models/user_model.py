from datetime import datetime

from ....database.db_con import connect
from psycopg2.extras import RealDictCursor


class Users:
    """ Contains methods for user models """

    def __init__(self):
        self.db = connect()

    def signup(self, firstname, lastname, othername, email, phoneNumber, username, password, isAdmin=None):
        """ creates user signup model """

        if isAdmin == None:
            isAdmin = False

        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = """ INSERT INTO users (firstname, lastname, othername, email, phoneNumber,
                username, password, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING * """

        cursor.execute(query, (firstname, lastname, othername, email, phoneNumber, username, password, isAdmin))
        user = cursor.fetchone()
        self.db.commit()
        cursor.close()


        return user

    def signin(self, userdata, username):
        """ creates user signin model """

        cursor = self.db.cursor(cursor_factory=RealDictCursor)
        query = " SELECT {} FROM users WHERE username = '{}' ".format(userdata, username)
        cursor.execute(query)
        data = cursor.fetchone()
        return data
