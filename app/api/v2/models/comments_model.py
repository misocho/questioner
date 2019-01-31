from app.api.v2.models.questions_model import Questions
from app.database.db_con import QuestionerDB


class Comments:
    """ contains methods for comments models """

    def add_comment(self, username, question_id, comment):
        """ contains model for posting a question """

        query = "SELECT title, body FROM questions WHERE id = {}".format(
            question_id)

        question_data = QuestionerDB.fetch_one(query)

        query_2 = """INSERT INTO comments (question_id, question_title,
        question_body, comment, username) VALUES (%s, %s, %s, %s, %s)
        RETURNING * """

        data = (question_id, question_data['title'], question_data['body'],
                comment, username)
        
        return QuestionerDB.save(query_2, data)
