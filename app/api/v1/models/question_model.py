questions = []


class QuestionModels():

    votes = 0
    def __init__(self):
        self.db = questions
        self.votes = QuestionModels.votes
        QuestionModels.votes + 1
    def post_question(self, meetup_id, postedby, body):
        """ method to post question """
        payload = {
            "meetup": meetup_id,
            "question_id": str(len(questions) + 1),
            "postedby": postedby,
            "body": body,
            "votes": self.votes
        }

        self.db.append(payload)
        return payload, {"message": "question was successsfully posted"}

    def upvote_question(self, question_id):
        """ method to upvote question """

        question = [
            question for question in self.db if question["question_id"] == question_id]
        if question:
            payload = {
                "meetupId": question[0]["meetup"],
                "body": question[0]["body"],
                "votes": self.votes
            }

            return payload, {"message": "upvote successfull"}
