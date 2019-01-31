from datetime import datetime
from app.database.db_con import QuestionerDB


class Meetups:
    """ contains methods for meetup models """

    def post_meetup(self, username, title, organizer, location,
                    happeningOn, tags, images):

        query = """INSERT INTO meetups (username, happeningOn, location,
        images, title, organizer,tags) VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING * """

        data = username, happeningOn, location,
        images, title, organizer, tags
        return QuestionerDB.save(query, data)

    def getall(self):
        """ contains method for getting one meetup """

        query = """ SELECT * FROM meetups """
        return QuestionerDB.fetch_all(query)

    def getOne(self, meetup_id, meetupdata):
        """ contains method for geting one meetup """

        query = " SELECT {} FROM meetups WHERE id = '{}'".format(
            meetupdata, meetup_id)

        return QuestionerDB.fetch_one(query)

    def remove(self, meetup_id):
        """ contains method for deleting a meetup """

        query = "DELETE FROM meetups WHERE id = '{}';".format(meetup_id)
        QuestionerDB.delete_one(query)

    def rsvp(self, meetup_id, username, response):
        """ contains method for making a meetup rsvp """

        query = "INSERT INTO rsvps (meetup_id, username, response) VALUES (%s, %s, %s) RETURNING id, username, response"

        data = (meetup_id, username, response)
        return QuestionerDB.save(query, data)

    def get_upcoming(self):
        """ method for getting upcoming meetups """

        now = datetime.now()

        query = "SELECT * from meetups WHERE happeningOn > '{}'".format(now)
        
        return QuestionerDB.fetch_all(query)
