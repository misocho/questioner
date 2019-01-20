from datetime import datetime

from ....database.db_con import connect


class Users:
    """ Contains methods for user models """

    def __init__(self):
        self.db = connect()

    def signup(self, firstname, lastname, othername, email, phoneNumber, username, password, isAdmin=False):
        """ creates user signup model """

        register = datetime.now()

        cursor = self.db.cursor()
        query = """ INSERT INTO users(firstname, lastname, othername, email, phoneNumber,
                username, isAdmin, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETUNING username"""
        
        cursor.execute(query, (firstname, lastname, othername, email, phoneNumber, username, password, isAdmin))

        cursor.fetchone()[0]
        self.db.commit()
        cursor.close()
        return username