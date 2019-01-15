from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import meetup_models

meetup_blueprint = Blueprint('meetup_blueprint', __name__, url_prefix='/api/v1')
meetups = meetup_models.MeetupModels()
rsvp = meetup_models.RsvpModels()
@meetup_blueprint.route('/create_meetup', methods=['POST'])
def create_meetup():
    """ endpoint for creating meetup"""
    try:
        meetup_data = request.get_json() if request.is_json else None
    except Exception:
        return jsonify({"message": "data not in json"}), 400

    if not meetup_data:
        return jsonify({"message": "Data set cannot be empty"}) , 202
    title = meetup_data.get('title')
    organizer = meetup_data.get('organizer')
    location = meetup_data.get('location')
    from_date = meetup_data.get('from_date')
    to_date = meetup_data.get('to_date')
    tags = meetup_data.get('tags')

    res = jsonify(meetups.create_meetup(title, organizer, location, from_date, to_date, tags))
    res.status_code = 201
    return res 

@meetup_blueprint.route('/meetups', methods=['GET'])
def getall():
    """ endpoint for get all meetups """

    data = meetups.getall_meetups()
    return make_response (jsonify({
        "message" : "Success",
        "meetups" : data
    }), 200)

@meetup_blueprint.route('/meetups/<meetupId>', methods=['GET'])
def getOne(meetupId):
    """ endpoint for get specific meetup """
    meetup = meetups.get_meetup(meetupId)
    if meetup:
        return make_response(jsonify({
            'message' : 'Success',
            'meetup' : meetup}), 200)
    return make_response(jsonify({'message' : 'meetup not found'}), 404)

@meetup_blueprint.route('/meetups/<meetupId>/rsvp', methods=['POST'])
def rsvp_meetup(meetupId):
    """ endpoint for rsvp meetup """
    try:
        data = request.get_json() if request.is_json else None
    except Exception:
        return jsonify({"message": "data not in json"}), 400

    userId = data.get('userId')
    meetupId = meetupId
    response  = data.get('response')

    res = rsvp.post_rsvp(userId, meetupId, response)
    return res