from psycopg2.extras import RealDictCursor
from app.database.db_con import QuestionerDB


class Questions:
    """ contains methods for questions models """

    def post_question(self, user, title, meetup_id, body):

        query = """ INSERT INTO questions (meetup_id, username, title, body) VALUES (%s, %s, %s, %s) RETURNING  id, createdOn, meetup_id, username, title, body, votes"""

        data = (meetup_id, user, title, body)
        return QuestionerDB.save(query, data)

    def getOne(self, question_id, questiondata):
        """ contains method for getting one question """

        query = " SELECT {} FROM questions WHERE id = '{}'".format(
            questiondata, question_id)

        return QuestionerDB.fetch_one(query)

    def up_vote(self, username, question_id):
        """ contains method for up-voting a question """

        query = """ UPDATE questions SET votes = votes+1 WHERE id = {} RETURNING * """.format(
            question_id)

        votes = QuestionerDB.update(query)
        return votes

    def down_vote(self, username, question_id):
        """ contains method for down-voting a question """

        query = """ UPDATE questions SET votes = votes-1 WHERE id = {} RETURNING * """.format(
            question_id)

        votes = QuestionerDB.update(query)
        return votes

    def save_votes(self, username, question_id):
        """ updates votes table """

        query = """ INSERT INTO votes (username, question_id) VALUES (%s, %s)RETURNING * """
        data = (username, question_id)
        QuestionerDB.save(query, data)


    def get_all(self):
        """ contains method for getting all questions """

        query = """SELECT * FROM questions """
        questions = QuestionerDB.fetch_all(query)

        return questions

    def get_meetup_questions(self, meetup_id):
        """ get questions relaed to a meetup """

        query = """ SELECT title as question_title, id as question_id, body as question_body, votes as question_votes, meetup_id FROM questions 
            WHERE meetup_id = '{}' ORDER BY votes DESC""".format(meetup_id)

        return QuestionerDB.fetch_all(query)
