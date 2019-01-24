from flask import Blueprint, jsonify, make_response, request
from app.api.v2.utils.auth import login_required
from app.api.v2.models.comments_model import Comments
from app.api.v2.utils.validations import Validations
from app.api.v2.models.questions_model import Questions

question = Questions()

comment_v2 = Blueprint('comment_v2', __name__, url_prefix='/api/v2')

comments = Comments()


@comment_v2.route('/<int:question_id>/comments', methods=['POST'])
@login_required
def post_comment(current_user, question_id):
    """ endpoint for posting a comment """
    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "error": "Data not in json"
        }), 400

    required = ['comment']

    for value in required:
        if not (data.get(value) and data.get(value).replace(' ', '')):
            return jsonify({
                "status": 400,
                "error": "Please provide {}".format(value)
            }), 400

        user = current_user
        comment = data.get('comment')

        search_question = question.getOne(question_id, "id")

        if search_question:
            res = comments.add_comment(current_user, question_id, comment)
            return jsonify({
                "data": [res],
                "status": 201
            })
        else:
            return jsonify({
                "status": 404,
                "error": "Question does not exist"
            }), 404
