from datetime import datetime

from ....database.db_con import connect


class Users:
    """ Contains methods for user models """

    def __init__(self):
        self.db = connect()

    def signup(self, firstname, lastname, othername, email, phoneNumber, username, password, isAdmin=None):
        """ creates user signup model """

        if isAdmin == None:
            isAdmin = False

        cursor = self.db.cursor()
        query = """ INSERT INTO users (firstname, lastname, othername, email, phoneNumber,
                username, password, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING registered"""

        cursor.execute(query, (firstname, lastname, othername, email, phoneNumber, username, password, isAdmin))
        registered = cursor.fetchone()[0]
        self.db.commit()
        cursor.close()


        user = {
            "firstname" : firstname,
            "lastname" : lastname,
            "othername" : othername,
            "email" : email,
            "phonenumber" : phoneNumber,
            "username" : username,
            "password" : password,
            "isAdmin" : isAdmin,
            "registered" : registered
        }
        
        return user

    def signin(self, userdata, username):
        """ creates user signin model """

        query = " SELECT {} FROM users WHERE username = '{}' ".format(userdata, username)

        return query
