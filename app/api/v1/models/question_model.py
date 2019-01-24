from .base_model import BaseModels, questions_list, meetups_list
from flask import jsonify
from ....validators import validator

question_validation = validator.BaseValidations()

class QuestionModels(BaseModels):

    def __init__(self):
        self.db = 'questions'

    def post_question(self, meetup_id, title, postedby, body):
        """ method to post question """

        if not question_validation.verifyinput(title):
            return jsonify ({"message" : "Please provide question title"}) , 400

        if not question_validation.verifyinput(body):
            return jsonify ({"message" : "Please provide question body"}) , 400

        if not question_validation.verifyinput(meetup_id):
            return jsonify ({"message" : "Please provide meetup_id"}), 400

        if not question_validation.verifyinput(postedby):
            return jsonify ({"message" : "Please provide postedby field"}), 400
        
        payload = {
            "meetup_id": meetup_id,
            "question_id": str(len(questions_list) + 1),
            "title" : title, 
            "postedby": postedby,
            "body": body,
            "up_votes": 0,
            "down_votes" : 0
        }
        for record in meetups_list:
            if record["meetup_id"] == meetup_id:
                self.save_data(payload)
                return jsonify(payload, {"message": "question was successsfully posted"}), 201
        return jsonify({"message" : "meetup does not exist"}), 404
        

    def upvote_question(self, question_id):
        """ method to upvote question """

        question = self.search_db("question_id", question_id)
        if question:
            question["up_votes"] += 1
            return jsonify(question, {"message": "upvote successful"}) , 200

        return jsonify({"message": "question not found"}), 404

    def downvote_question(self, question_id):
        """ method to downvote question """

        question = self.search_db("question_id", question_id)
        if question:
            question["down_votes"] += 1

            return jsonify(question, {"message": "downvote successful"}) , 200

        return jsonify({"message": "question not found"}), 404
