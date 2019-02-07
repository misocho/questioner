from flask import Blueprint, jsonify, make_response, request
from app.api.v2.models.upload_model import UploadImage
from app.api.v2.utils.auth import admin_required
from app.api.v2.models.meetup_model import Meetups

upload = Blueprint('upload', __name__, url_prefix='/api/v2')

meetup = Meetups()
img = UploadImage()

@upload.route('/meetups/<int:meetup_id>/img', methods=['POST'])
@admin_required
def uploadImage(meetup_id, current_user):
    """ endpoint for uploading an image """

    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "error": "Data not in json"
        }), 400

    required = ['image', 'extension']

    for value in required:
        if not (data.get(value) and data.get(value).replace(' ', '')):
            return jsonify({
                "status": 400,
                "error": "Please provide {}".format(value)
            }), 400

    image = data.get('image')
    extension = data.get('extension')
    meetup_data = "id"
    search_meetup = meetup.getOne(meetup_id, meetup_data)

    if search_meetup:
        data = img.saveToImage(meetup_id, imageFile=image, extension=extension)
        return jsonify({
            'data': [data],
            "status": 201,
            "message": "Image was successfully uploaded"
        }), 201

    else:
        return jsonify(
            {
                "error": "Meetup {} does not exist".format(meetup_id),
                "status": 404
            }, 404
        )