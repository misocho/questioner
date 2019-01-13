from flask import Flask, Blueprint, request, jsonify, make_response
from ..models import meetup_models

meetup_blueprint = Blueprint('meetup_blueprint', __name__, url_prefix='/api/v1')
meetups = meetup_models.MeetupModels()
rsvp = meetup_models.RsvpModels()
@meetup_blueprint.route('/create_meetup', methods=['POST'])
def create_meetup():
    """ endpoint for creating meetup"""

    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"}) , 202
    title = data.get('title')
    organizer = data.get('organizer')
    location = data.get('location')
    from_date = data.get('from_date')
    to_date = data.get('to_date')
    tags = data.get('tags')

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
    data = request.get_json()

    userId = data.get('userId')
    meetupId = meetupId
    response  = data.get('response')

    res = rsvp.post_rsvp(userId, meetupId, response)
    return res