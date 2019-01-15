from .base_model import BaseModels, questions_list, meetups_list
from flask import jsonify


class QuestionModels(BaseModels):

    def __init__(self):
        self.db = 'questions'

    def post_question(self, meetup_id, postedby, body):
        """ method to post question """
        payload = {
            "meetup": meetup_id,
            "question_id": str(len(questions_list) + 1),
            "postedby": postedby,
            "body": body,
            "votes": 0
        }
        for record in meetups_list:
             if record["meetup_id"]== meetup_id:
                return jsonify({"message" : "meetup does not exist"}), 404
        self.save_data(payload)
        return jsonify(payload, {"message": "question was successsfully posted"}), 201

    def upvote_question(self, question_id):
        """ method to upvote question """

        question = self.search_db("question_id", question_id)
        if question:
            question["votes"] += 1

            return jsonify(question, {"message": "upvote successfull"}) , 201

        return jsonify({"message": "question not found"}), 404

    def downvote_question(self, question_id):
        """ method to downvote question """

        question = self.search_db("question_id", question_id)
        if question:
            question["votes"] -= 1

            return jsonify(question, {"message": "downvote successfull"}) , 201

        return jsonify({"message": "question not found"}), 404
