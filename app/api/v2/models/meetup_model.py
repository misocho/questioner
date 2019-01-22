from datetime import datetime


from ....database.db_con import connect
from psycopg2.extras import RealDictCursor

class Meetups:
    """ contains methods for meetup models """

    def post_meetup(self, username, title, organizer, location, happeningOn, tags, images):
        db = connect()

        cursor = db.cursor(cursor_factory=RealDictCursor)
        
        query = """ INSERT INTO meetups (username, happeningOn, location, images, title, organizer,
                tags) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING * """

        cursor.execute(query, (username, happeningOn, location, images, title, organizer, tags))  
        meetup_data = cursor.fetchone()
        db.commit()
        cursor.close()

        return meetup_data 


    def getall(self):

        cursor = connect().cursor(cursor_factory=RealDictCursor)

        query = """ SELECT * FROM meetups """
        cursor.execute(query)
        meetups = cursor.fetchall()
        return meetups