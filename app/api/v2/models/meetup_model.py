from datetime import datetime
from app.database.db_con import QuestionerDB
from app.api.v2.models.questions_model import Questions

q = Questions()


class Meetups:
    """ contains methods for meetup models """

    def post_meetup(self, username, title, organizer, location,
                    happeningOn):

        query = """INSERT INTO meetups (username, happeningOn, location,
        title, organizer) VALUES (%s, %s, %s, %s, %s)
        RETURNING * """

        data = (username, happeningOn, location, title, organizer)

        return QuestionerDB.save(query, data)

    def getall(self):
        """ contains method for getting one meetup """

        query = """ SELECT * FROM meetups """
        return QuestionerDB.fetch_all(query)

    def getOne(self, meetup_id, meetupdata):
        """ contains method for geting one meetup """

        query = " SELECT {} FROM meetups WHERE id = '{}'".format(
            meetupdata, meetup_id)
        meetup = QuestionerDB.fetch_one(query)
        question = dict(questions=q.get_meetup_questions(meetup_id))

        return {**meetup, **question}

    def delete_question(self, meetup_id):
        """ Deletes questions of relvant meetups """

        query = """ DELETE FROM questions WHERE
         meetup_id = '{}' """.format(meetup_id)

        QuestionerDB.delete_one(query)

    def remove(self, meetup_id):
        """ contains method for deleting a meetup """

        query = "DELETE FROM meetups WHERE id = '{}';".format(meetup_id)
        query1 = """SELECT * FROM questions 
        WHERE meetup_id = {}""".format(meetup_id)

        questions = QuestionerDB.fetch_all(query1)
        if questions:
            self.delete_question(meetup_id)
        
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
