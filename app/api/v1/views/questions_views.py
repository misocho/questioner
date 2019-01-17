from flask import Flask, Blueprint, request, jsonify, make_response
from ....validators import validator
from ..models import question_model

question_validation = validator.BaseValidations()

question_blueprint = Blueprint('question_blueprint', __name__, url_prefix='/api/v1')
questions = question_model.QuestionModels()

@question_blueprint.route('/questions', methods=['POST'])
def post_question():
    """ endpoint for posting question """


    try:
        data = request.get_json() if request.is_json else None
    except Exception:
        return jsonify({"message": "data not in json"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"message" : "Data set cannot be empty"}), 400
    meetup_id = data.get('meetup_id')
    postedby = data.get('postedby')
    body = data.get('body')

    if not question_validation.input_provided(body) or body.isspace():
        return jsonify ({"message" : "Please provide question body"}) , 400

    if not question_validation.input_provided(meetup_id) or meetup_id.isspace():
            return jsonify ({"message" : "Please provide meetup_id"}), 400
    if not question_validation.input_provided(postedby) or postedby.isspace():
            return jsonify ({"message" : "Please provide postedby field"}), 400
        
    return questions.post_question(meetup_id, postedby, body)
    

@question_blueprint.route('/questions/<question_id>/upvote', methods=['PATCH'])
def upvote(question_id):
    """ endpoint for upvote question """
    question_id = question_id
    res = questions.upvote_question(question_id)

    return res

@question_blueprint.route('/questions/<question_id>/downvote', methods=['PATCH'])
def downvote(question_id):
    """ endpoint for downvote question """
    question_id = question_id
    res = questions.downvote_question(question_id)

    return res
