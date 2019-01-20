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
                username, password, isAdmin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING username"""
        
        cursor.execute(query, (firstname, lastname, othername, email, phoneNumber, username, password, isAdmin))

        self.db.commit()
        cursor.close()
        return username