from app.database.db_con import QuestionerDB
from psycopg2.extras import RealDictCursor
from flask import jsonify


class Validations:
    """ This class contains validation methods """

    def check_exist(self, table, value, item):
        """ Method to check if a value exists in the database """

        query = "SELECT {1} FROM {0} WHERE {1} = '{2}'".format(
            table, value, item)

        data = QuestionerDB.fetch_one(query)

        if data:
            return jsonify({
                "status": 409,
                "message": "{} already exists".format(item)
            }), 409
        else:
            return False

    def made_rsvp(self, table, meetup_id, username):
        """ method to check if user made a rsvp """

        query = "SELECT username FROM {0} WHERE meetup_id = {1}".format(
            table, meetup_id)

        rsvp = QuestionerDB.fetch_one(query)

        if rsvp:
            if username in rsvp:
                return True
        else:
            return False

    def voted(self, username, vote, question_id):
        """ method to check if user has voted """

        query = "SELECT username FROM votes WHERE question_id = {}".format(
            question_id)

        voted = QuestionerDB.fetch_all(query)

        for value in voted:
            if value["username"] == username:
                return True
        return False

    def check_vote(self, vote, username):
        """ method to check vote """

        query = "SELECT vote FROM votes WHERE username = '{}'".format(
            username)

        votes = QuestionerDB.fetch_all(query)

        for value in votes:
            if value["vote"] == vote:
                return True
        return False

    def posted_meetup(self, title, happeningOn, location):
        """ method to check if meetup is posted """

        query = "SELECT title, happeningOn, location FROM meetups"

        posted = QuestionerDB.fetch_all(query)

        for meetup in posted:
            if (meetup["happeningon"], meetup["title"], meetup["location"]) == (happeningOn, title, location):
                return True

        return False

    def posted_question(self, title, body, meetup_id):
        """ method to check if a question is posted """

        query = "SELECT title, body, meetup_id FROM questions"

        questions = QuestionerDB.fetch_all(query)

        for question in questions:
            if (question["title"], question["body"], question["meetup_id"]) == (title, body, meetup_id):
                return True

        return False
