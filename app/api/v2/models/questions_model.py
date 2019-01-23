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
