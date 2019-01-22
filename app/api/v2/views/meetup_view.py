from flask import Blueprint, jsonify, make_response, request
from app.api.v2.utils.auth import login_required

from ..models.meetup_model import Meetups

meetup_v2 = Blueprint('meetup_v2', __name__, url_prefix='/api/v2')


meetup = Meetups()


@meetup_v2.route('/meetups', methods=['POST'])
def create_meetup():
    """ endpoint for posting a meetup"""
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

    res = meetup.post_meetup(username, title, organizer,
                             location, happeningOn, tags, images)

    return jsonify({
        "data": [res],
        "status": 201,
        "message": "meetup was successfully posted"
    }), 201


@meetup_v2.route('/meetups')
@login_required
def all_meetups(current_user, isAdmin):
    """ endpoint for getting all meetups """
    res = meetup.getall()

    return jsonify({
        "user": current_user,
        "isAdmin" : isAdmin,
        "data": res,
        "status": 200
    }), 200


@meetup_v2.route('/meetups/<meetup_id>')
def get_one(meetup_id):
    """ endpoint for getting one meetup """

    meetupdata = "id, title, location, happeningOn, tags"
    res = meetup.getOne(meetup_id, meetupdata)
    if res:
        return jsonify({
            "status": 200,
            "data": res
        }), 200
    else:
        return jsonify({
            "status": 404,
            "message": "Meetup does not exist"
        }), 404
