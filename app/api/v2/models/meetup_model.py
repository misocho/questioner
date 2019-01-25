from datetime import datetime


from ....database.db_con import connect
from psycopg2.extras import RealDictCursor


class Meetups:
    """ contains methods for meetup models """

    def post_meetup(self, username, title, organizer, location,
                    happeningOn, tags, images):
        db = connect()

        cursor = db.cursor(cursor_factory=RealDictCursor)

        query = """INSERT INTO meetups (username, happeningOn, location,
        images, title, organizer,tags) VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING * """
        
        cursor.execute
        cursor.execute(query, (username, happeningOn, location,
                               images, title, organizer, tags))
        meetup_data = cursor.fetchone()
        db.commit()
        cursor.close()

        return meetup_data

    def getall(self):
        """ contains method for getting one meetup """
        cursor = connect().cursor(cursor_factory=RealDictCursor)

        query = """ SELECT * FROM meetups """
        cursor.execute(query)
        meetups = cursor.fetchall()
        return meetups

    def getOne(self, meetup_id, meetupdata):
        """ contains method for geting one meetup """
        cursor = connect().cursor(cursor_factory=RealDictCursor)

        query = " SELECT {} FROM meetups WHERE id = '{}'".format(
            meetupdata, meetup_id)

        cursor.execute(query)
        data = cursor.fetchone()
        return data

    def remove(self, meetup_id):
        """ contains method for deleting a meetup """
        db = connect()
        cursor = db.cursor(cursor_factory=RealDictCursor)

        query = "DELETE FROM meetups WHERE id = '{}';".format(meetup_id)

        cursor.execute(query)
        db.commit()
        cursor.close()

    def rsvp(self, meetup_id, username, response):
        """ contains method for making a meetup rsvp """
        db = connect()
        cursor = db.cursor(cursor_factory=RealDictCursor)

        query = "INSERT INTO rsvps (meetup_id, username, response) VALUES (%s, %s, %s) RETURNING id, username, response"

        cursor.execute(query, (meetup_id, username, response))
        rsvp_data = cursor.fetchone()
        db.commit()
        cursor.close()

        return rsvp_data

    def get_upcoming(self):
        """ method for getting upcoming meetups """

        meetups = self.getall()

        db = connect()
        cursor = db.cursor(cursor_factory=RealDictCursor)

        now = datetime.now()

        query = "SELECT * from meetups WHERE happeningOn > '{}'".format(now)
        cursor.execute(query)
        meetups = cursor.fetchall()
        return meetups


