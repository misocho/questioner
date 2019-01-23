from flask import Blueprint, jsonify, make_response, request
from app.api.v2.utils.auth import login_required
from app.api.v2.models.questions_model import Questions


quest_v2 = Blueprint('quest_v2', __name__, url_prefix='/api/v2')

question = Questions()


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

    required = ['title', 'meetup_id', 'body']

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

    res = question.post_question(user, title, meetup_id, body)

    return jsonify({
        "data": [res],
        "status": 201
    }), 201