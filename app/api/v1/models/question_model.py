from .base_model import BaseModels
questions = []


class QuestionModels(BaseModels):
    
    def __init__(self):
        self.db = questions
    def post_question(self, meetup_id, postedby, body):
        """ method to post question """
        payload = {
            "meetup": meetup_id,
            "question_id": str(len(questions) + 1),
            "postedby": postedby,
            "body": body,
            "votes": 0
        }

        self.db.append(payload)
        return payload, {"message": "question was successsfully posted"}

    def upvote_question(self, question_id):
        """ method to upvote question """

        question = self.check_item(question_id, "question_id", self.db)
        if question:
            question[0]["votes"] += 1

            return question, {"message": "upvote successfull"}

    def downvote_question(self, question_id):
        """ method to downvote question """

        question = self.check_item(question_id, "question_id", self.db)
        if question:
            question[0]["votes"] -= 1

            return question, {"message": "downvote successfull"}
