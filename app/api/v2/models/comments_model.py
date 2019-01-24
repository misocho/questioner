from add.database.db_con import connect
from psycopg2.extras import RealDictCursor

class Comments:
    """ contains methods for comments models """

    def post_comment(self, username, question_id, comment):
        """ contains model for posting a question """

        db = connect()

        cursor = db.cursor(cursor_factory=RealDictCursor)

        query = "SELECT title, body FROM questions WHERE id = {}".format(question_id)

        cursor.execute(query)
        question_data = cursor.fetchone()

        query_2 = """INSERT INTO comments (question_id, question_title, question_body, comment, username) VALUES (%s, %s, %s, %s, %s) RETURNING * """

        cursor.execute(query_2, (question_id, question_data['title'], question_data['body'], comment, username))
        comment = cursor.fetchone()
        return comment
        