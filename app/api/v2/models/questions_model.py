from app.database.db_con import connect
from psycopg2.extras import RealDictCursor


class Questions:
    """ contains methods for questions models """

    def post_question(self, user, title, meetup_id, body):

        db = connect()

        cursor = db.cursor(cursor_factory=RealDictCursor)

        query = """ INSERT INTO questions (meetup_id, username, title, body) VALUES (%s, %s, %s, %s) RETURNING  id, createdOn, meetup_id, username, title, body, votes"""

        cursor.execute(query, (meetup_id, user, title, body))
        question_details = cursor.fetchall()
        db.commit()
        cursor.close()

        return question_details

    def getOne(self, question_id, questiondata):
        """ contains method for getting one question """
        cursor = connect().cursor(cursor_factory=RealDictCursor)

        query = " SELECT {} FROM questions WHERE id = '{}'".format(
            questiondata, question_id)

        cursor.execute(query)
        data = cursor.fetchone()
        return data

    def up_vote(self, username, question_id):
        """ contains method for up-voting a question """
        db = connect()

        cursor = db.cursor(cursor_factory=RealDictCursor)

        query_1 = """ INSERT INTO votes (username, question_id) VALUES (%s, %s) """

        query_2 = """ UPDATE questions SET votes = votes+1 WHERE id = {} RETURNING * """.format(
            question_id)

        cursor.execute(query_2)
        data = cursor.fetchone()

        cursor.execute(query_1, (username, question_id))
        db.commit()
        cursor.close()

        return data

    def down_vote(self, username, question_id):
        """ contains method for down-voting a question """
        db = connect()

        cursor = db.cursor(cursor_factory=RealDictCursor)

        query_1 = """ INSERT INTO votes (username, question_id) VALUES (%s, %s) """

        query_2 = """ UPDATE questions SET votes = votes-1 WHERE id = {} RETURNING * """.format(
            question_id)

        cursor.execute(query_2)
        data = cursor.fetchone()

        cursor.execute(query_1, (username, question_id))
        db.commit()
        cursor.close()

        return data