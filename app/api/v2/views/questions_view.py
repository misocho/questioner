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

    check_meetup = meetup.getOne(meetup_id, "id")  # checks if meetup exists
    if check_meetup:

        try:
            res = question.post_question(current_user, title, meetup_id, body)

            return jsonify({
                "data": res,
                "status": 201
            }), 201

        except:
            return jsonify({
                "error": "Question already exists",
                "status": 409
            }), 409

    else:
        return jsonify({
            "error": "Meetup {} does not exist".format(meetup_id),
            "status": 404
        }), 404


@quest_v2.route('/questions/<int:question_id>/upvote', methods=['PATCH'])
@login_required
def upvote(question_id, current_user):
    """ endpoint for upvoting a question """
    questiondata = "id"
    # checks if the question exists
    search_question = question.getOne(question_id, questiondata)

    if search_question:
        if q_validate.voted(current_user, question_id):
            return jsonify({
                "error": "User {} has already voted for question {}".format(current_user, question_id),
                "status": 409
            }), 409
        else:
            vote = question.up_vote(current_user, question_id)
            question.save_votes(current_user, question_id)
        return jsonify({
            "data": [vote],
            "status": 200
        }), 200

    else:
        return jsonify({
            "error": "Question {} does not exist".format(question_id),
            "status": 404
        }), 404


@quest_v2.route('/questions/<int:question_id>/downvote', methods=['PATCH'])
@login_required
def downvote(question_id, current_user):
    """ endpoint for downvoting a question """
    questiondata = "id"
    # checks if the question exists
    search_question = question.getOne(question_id, questiondata)

    if search_question:
        if q_validate.voted(current_user, question_id):
            return jsonify({
                "error": "User {} has already voted for question {}".format(current_user, question_id),
                "status": 409
            }), 409
        else:
            vote = question.down_vote(current_user, question_id)
            question.save_votes(current_user, question_id)
        return jsonify({
            "data": [vote], 
            "status": "200"
            }), 200

    else:        
        return jsonify({
            "error": "Question {} does not exist".format(question_id),
            "status": 404
        }), 404



@quest_v2.route('/questions/<int:question_id>', methods=['GET'])
@login_required
def getQuestion(question_id, current_user):
    """ endpoint for getting one question """

    questiondata = "*"

    get_question = question.getOne(question_id, questiondata)

    if get_question:
        return jsonify({
            "data": get_question,
            "status": 200
        }), 200

    else:
        return jsonify({
            "error": "Question {} does not exist".format(question_id),
            "status": 404
        })

@quest_v2.route('/questions')
@login_required
def get_questions(current_user):
    """ endpoint for getting all questions """

    res = question.get_all()

    return jsonify({
        "data": [res],
        "status": 200
    }), 200