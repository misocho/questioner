questions = []

class QuestionModels():
    def __init__(self):
        self.db = questions
        self.votes = 0

    def post_question(self, meetup_id, postedby, body):
        """ method to post question """
        payload = {
            "meetup" : meetup_id,
            "question_id" : str(len(questions) + 1),
            "postedby" : postedby, 
            "body" : body,
            "votes" : self.votes
        }

        self.db.append(payload)
        return payload, {"message" : "meetup wad created succeccfilly"}