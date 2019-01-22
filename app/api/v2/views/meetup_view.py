from flask import Blueprint, jsonify, make_response, request


from ..models.meetup_model import Meetups

meetup_v2 = Blueprint('meetup_v2', __name__, url_prefix='/api/v2')


meetup = Meetups()


@meetup_v2.route('/meetups', methods=['POST'])
def create():
    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "message": "Data not injson"
        }), 400

    username = data.get('username')
    title = data.get('title')
    organizer = data.get('organizer')
    location = data.get('location')
    happeningOn = data.get('happeningOn')
    tags = data.get('tags')
    images = data.get('images')

    res = meetup.post_meetup(username, title, organizer, location, happeningOn, tags, images)
    
    return jsonify({
        "data" : [res],
        "status" : 201,
        "message" : "registration was successful"
    }) , 201