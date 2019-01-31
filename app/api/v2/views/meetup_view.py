from flask import Blueprint, jsonify, make_response, request
from app.api.v2.utils.auth import login_required, admin_required
from ..models.meetup_model import Meetups
from app.api.v2.utils.validations import Validations
from datetime import datetime

val = Validations()

meetup_v2 = Blueprint('meetup_v2', __name__, url_prefix='/api/v2')


meetup = Meetups()


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
        
    if happeningOn < datetime.now():
        return jsonify({
            "error": "Meetup can not take place in the past",
            "status": 409
        }), 409
    tags = data.get('tags')
    images = data.get('images')

    try:
        res = meetup.post_meetup(username, title, organizer,
                             location, happeningOn, tags, images)

    except:
        return jsonify({
            "error": "Meetup already exists",
            "status": 409
        }), 409

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


@meetup_v2.route('meetups/<int:meetup_id>/rsvp', methods=['POST'])
@login_required
def rsvp_meetup(meetup_id, current_user):
    """ endpoint for rsvp meetup """

    try:
        data = request.get_json()

    except:
        return jsonify({
            "status": 400,
            "error": "Data not in json"
        }), 400

    if not (data.get('rsvp') and data.get('rsvp').replace(' ', '')):
        return jsonify({
            "error": "Please provide an rsvp",
            "status": 400
        }), 400

    response = data.get('rsvp')

    meetupdata = "id"
    search_meetup = meetup.getOne(meetup_id, meetupdata)

    if search_meetup:  # checks if meetup exists
        made_rsvp = val.made_rsvp('rsvps', meetup_id, current_user)
        if not made_rsvp:  # checks is the user has already made a RSVP

            # checks if user input is a yes, no, or maybe
            if response not in ['yes', 'no', 'maybe']:
                return jsonify({
                    "error": "Your response should be either a yes, no, or maybe",
                    "status": 400
                }), 400

            response = meetup.rsvp(meetup_id, current_user, response)

            if response:
                return jsonify({
                    "data": [response],
                    "status": 201,
                    "message": "RSVP was successfull"
                }), 201
        else:
            return jsonify({
                "error": "{} already made a rsvp for meetup {}".format(current_user, meetup_id),
                "status": 409
            }), 409

    else:
        return jsonify(
            {
                "error": "Meetup {} does not exist".format(meetup_id),
                "status": 404
            }
        ), 404


@meetup_v2.route('meetups/upcoming')
@login_required
def get_upcoming(current_user):

    res = meetup.get_upcoming()

    return jsonify({
        "data": [res],
        "status": 200
    }), 200
