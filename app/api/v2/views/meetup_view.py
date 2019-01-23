from flask import Blueprint, jsonify, make_response, request
from app.api.v2.utils.auth import login_required, admin_required
from flask_restful.reqparse import RequestParser
from ..models.meetup_model import Meetups
from app.api.v2.utils.validations import Validations
from datetime import datetime


val = Validations()

meetup_v2 = Blueprint('meetup_v2', __name__, url_prefix='/api/v2')


meetup = Meetups()
parser = RequestParser()


@meetup_v2.route('/meetups', methods=['POST'])
@admin_required
def create_meetup(current_user):
    """ endpoint for posting a meetup"""
    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "error": "Data not in json"
        }), 400

    required = ['title', 'organizer',
                'location', 'happeningOn']

###### checks if all required fields are provided #####
    for value in required:
        if not (data.get(value) and data.get(value).replace(' ', '')):
            return jsonify({
                "status": 400,
                "error": "Please provide {}".format(value)
            }), 400

    username = current_user
    title = data.get('title')
    organizer = data.get('organizer')
    location = data.get('location')

    try:
        happeningOn = datetime.strptime(
            data.get('happeningOn'), r'%m-%d-%Y %I:%M%p')
    except:
        return jsonify({
            "error": "Time should be in the format mm-dd-yyy H:Mam/pm",
            "status": 400
        })
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
def all_meetups(current_user):
    """ endpoint for getting all meetups """
    res = meetup.getall()

    return jsonify({
        "data": res,
        "status": 200
    }), 200


@meetup_v2.route('/meetups/<int:meetup_id>')
@login_required
def get_one(meetup_id, current_user):
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
            "error": "Meetup does not exist"
        }), 404


@meetup_v2.route('meetups/<int:meetup_id>', methods=['DELETE'])
@admin_required
def delete_meetup(meetup_id, current_user):
    """ endpoint for deleting a meetup """

    meetup.remove(meetup_id)

    return jsonify(
        {"status": 200,
         "message": "meetup id {} was successfully deleted".format(meetup_id)
         }
    ), 200
