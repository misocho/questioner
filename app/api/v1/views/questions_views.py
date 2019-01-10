from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import question_model

question_blueprint = Blueprint('question_blueprint', __name__, url_prefix='/api/v1')
questions = question_model.QuestionModels()

@question_blueprint.route('/questions', methods=['POST'])
def post_question():
    """ endpoint for posting question """

    data = request.get_json()
    if not data:
        return jsonify({"message" : "Data set cannot be empty"})
    meetup_id = data.get('meetup_id')
    postedby = data.get('postedby')
    body = data.get('body')

    res = jsonify(questions.post_question(meetup_id, postedby, body))
    res.status_code = 201
    return res

@question_blueprint.route('/questions/<question_id>/upvote', methods=['POST'])
def upvote(question_id):
    """ endpoint for upvote question """
    question_id = question_id
    res = jsonify(questions.upvote_question(question_id))
    res.status_code = 201
    return res

@question_blueprint.route('/questions/<question_id>/downvote', methods=['POST'])
def downvote(question_id):
    """ endpoint for downvote question """
    question_id = question_id
    res = jsonify(questions.downvote_question(question_id))
    res.status_code = 201
    return res