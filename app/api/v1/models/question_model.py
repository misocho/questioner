questions = []


class QuestionModels():
    
    def __init__(self):
        self.db = questions
        self.votes = 0
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
                "votes": self.votes + 1
            }

            return payload, {"message": "upvote successfull"}

    def downvote_question(self, question_id):
        """ method to downvote question """

        question = [
            question for question in self.db if question["question_id"] == question_id]
        if question:
            payload = {
                "meetupId": question[0]["meetup"],
                "body": question[0]["body"],
                "votes": self.votes - 1
            }

            return payload, {"message": "downvote successfull"}
