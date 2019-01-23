from app.database.db_con import connect
from psycopg2.extras import RealDictCursor


class Questions:
    """ contains metods for questions models """

    def post_question(self, user, title, meetup_id, body):

        db = connect()

        cursor = db.cursor(cursor_factory=RealDictCursor)

        query = """ INSERT INTO questions (meetup_id, username, title, body) VALUES (%s, %s, %s, %s) RETURNING  createdOn, meetup_id, username, title, body, votes"""

        cursor.execute(query, (meetup_id, user, title, body))
        question_details = cursor.fetchall()
        db.commit()
        cursor.close()

        return question_details

    def up_vote(self, username, question_id):

        db = connect()

        cursor = db.cursor(cursor_factory=RealDictCursor)

        query_1 = """ INSERT INTO votes (username, question_id) VALUES (%s, %s) """

        query_2 = """ UPDATE questions SET votes = %s WHERE question_id = %s """

        cursor.execute(query_1, (username, question_id))
        db.commit()

        cursor.close()
