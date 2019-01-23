from ....database.db_con import connect
from psycopg2.extras import RealDictCursor
from flask import jsonify


class Validations:
    """ This class contains validation methods """

    def check_exist(self, table, value, item):
        """ Method to check if a value exists in the database """
        cursor = connect().cursor(cursor_factory=RealDictCursor)
        query = "SELECT {1} FROM {0} WHERE {1} = '{2}'".format(
            table, value, item)

        cursor.execute(query)
        data = cursor.fetchone()

        if data:
            return jsonify({
                "status": 409,
                "message": "{} already exists".format(item)
            }), 409
        else:
            return False

    def made_rsvp(self, table, meetup_id, username):
        """ method to check if user made a rsvp """
        cursor = connect().cursor()

        query = "SELECT username FROM {0} WHERE meetup_id = {1}".format(
            table, meetup_id)

        cursor.execute(query)
        data = cursor.fetchone()

        if data:
            if username in data:
                return True
        else:
            return False
