from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import question_model


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
    meetup_id = str(data.get('meetup_id'))
    postedby = data.get('postedby')
    body = data.get('body')
    title = data.get('title')

   
        
    return questions.post_question(meetup_id, title, postedby, body)
    

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
