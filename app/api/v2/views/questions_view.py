from flask import Blueprint, jsonify, make_response, request
from app.api.v2.utils.auth import login_required
from app.api.v2.models.questions_model import Questions
from app.api.v2.models.meetup_model import Meetups
from app.api.v2.utils.validations import Validations

quest_v2 = Blueprint('quest_v2', __name__, url_prefix='/api/v2')

question = Questions()
meetup = Meetups()

q_validate = Validations()


@quest_v2.route('/questions', methods=['POST'])
@login_required
def post_question(current_user):
    """ endpoint for posting a question """
    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "error": "Data not in json"
        }), 400

    required = ['title', 'body']
    if not data.get('meetup_id'):
        return jsonify({
            "status": 400,
            "error": "Please provide a meetup_id"
        }), 400

###### checks if all required fields are provided #####
    for value in required:
        if not (data.get(value) and data.get(value).replace(' ', '')):
            return jsonify({
                "status": 400,
                "error": "Please provide {}".format(value)
            }), 400

    user = current_user
    title = data.get('title')
    meetup_id = data.get('meetup_id')
    body = data.get('body')

    check_meetup = meetup.getOne(meetup_id, "id")
    if check_meetup:

        res = question.post_question(current_user, title, meetup_id, body)

        return jsonify({
            "data": res,
            "status": 201
        }), 201

    else:
        return jsonify({
            "error": "Meetup {} does not exist".format(meetup_id),
            "status": 404
        }), 404


@quest_v2.route('/questions/<int:question_id>/upvote', methods=['PATCH'])
@login_required
def upvote(question_id, current_user):

    questiondata = "id"
    search_question = question.getOne(question_id, questiondata)

    if search_question:
        voted = q_validate.voted(current_user, question_id)
        if not voted:
            vote = question.up_vote(current_user, question_id)
            return jsonify(vote)

        else:
            return jsonify({
                "error": "user {} has alrerady voted for question {}".format(current_user, question_id),
                "status": 409
            }), 409

    else:
        return jsonify({
            "error": "Question {} does not exist".format(question_id),
            "status": 404
        }), 404


@quest_v2.route('/questions/<int:question_id>', methods=['GET'])
@login_required
def getQuestion(question_id, current_user):

    questiondata = "*"

    get_question = question.getOne(question_id, questiondata)

    if question:
        return jsonify({
            "data": get_question,
            "status": 200
        }), 200

    else:
        return jsonify({
            "error": "QUestion {} does not exist".format(question_id),
            "status": 404
        })
